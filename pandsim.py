import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize,BoundaryNorm
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.gridspec import GridSpec
from scipy.sparse import lil_matrix
from IPython.display import HTML
from IPython.display import display
import random

class population():
    def __init__(self, N=100, duration=100, transmission_time=7, imunity_time=7, r_0=0.01, infection_rate=0.3,
                 mortality_rate=0.03, sociability=4, daily_contact_rate=0.5):
        self.N = N  # defining all parameters and initializing the world
        self.duration = duration
        self.transmission_time = transmission_time
        self.imunity_time = imunity_time
        self.sociability = sociability
        self.mortality_rate = mortality_rate
        self.daily_contact_rate = daily_contact_rate
        self.r_0 = r_0
        self.infection_rate = infection_rate
        self.history = []
        self.per = []
        self.death = []
        self.world = np.zeros((N, N), dtype=[('health', 'float32'), ('status', 'uint8'), ('timer', 'int32')])
        self.world['health'] = np.random.uniform(0.5, 1, (N, N))
        self.world[
            'timer'] = -imunity_time  # the world is created through a two dimensional structered array with the three fields healt,status,timer
        for _ in range(round(r_0 * N ** 2)):
            i, j = np.random.randint(N), np.random.randint(N)
            self.world['status'][i, j] = 1  # set status
            self.world['timer'][i, j] = self.transmission_time  # set time to transmit disease
        self.infection_chance_matrices = [
            np.random.uniform(0, 0.5, (2 * self.sociability + 1, 2 * self.sociability + 1)) for _ in range(3000)]
        self.contact_sphere = [
            np.random.uniform(0, 1, (2 * self.sociability + 1, 2 * self.sociability + 1)) < self.daily_contact_rate for
            _ in range(3000)]

    def neighbourhood(self, x, y):
        start_y = (y - self.sociability) % self.N
        end_y = (y + self.sociability + 1) % self.N
        start_x = (x - self.sociability) % self.N
        end_x = (x + self.sociability + 1) % self.N
        # Check if wrapping is needed
        if start_y > end_y:
            sub_world_y = np.concatenate([self.world[start_y:], self.world[:end_y]], axis=0)
        else:
            sub_world_y = self.world[start_y:end_y]
        if start_x > end_x:
            sub_world = np.concatenate([sub_world_y[:, start_x:], sub_world_y[:, :end_x]], axis=1)
        else:
            sub_world = sub_world_y[:, start_x:end_x]

        return sub_world['health'], sub_world['status'], sub_world['timer']

    def susceptibility(self, health_matrix, status_matrix, recovery_matrix):
        susceptible_condition = (status_matrix == 0) & (recovery_matrix < -self.imunity_time) & (
            random.choice(self.contact_sphere))
        infection_chance_matrix = random.choice(self.infection_chance_matrices)[:health_matrix.shape[0],
                                  :health_matrix.shape[1]]
        return susceptible_condition, infection_chance_matrix

    def infect(self, health_matrix, status_matrix, susceptible_condition, infection_chance_matrix):
        infection_chance = health_matrix - infection_chance_matrix  # Apply the random transmission factor
        infection_condition = infection_chance < self.infection_rate
        new_infections = infection_condition & susceptible_condition
        new_diseased = infection_condition & (infection_chance < self.infection_rate * self.mortality_rate)
        return new_infections, new_diseased

    def sim(self):
        plt.ion()
        t = 0
        dt = 1
        while t < self.duration:
            infected_indices = np.where(self.world['status'] == 1)
            for x, y in zip(*infected_indices):
                health_matrix, status_matrix, recovery_matrix = self.neighbourhood(x, y)
                susceptible_condition, infection_chance_matrix = self.susceptibility(health_matrix, status_matrix,
                                                                                     recovery_matrix)
                new_infections, new_diseased = self.infect(health_matrix, status_matrix, susceptible_condition,
                                                           infection_chance_matrix)
                status_matrix[new_infections] = 1
                recovery_matrix[new_infections] = self.transmission_time * (
                        2 / (3 * health_matrix[self.sociability, self.sociability]))
                status_matrix[new_diseased] = 2
            self.world['timer'] -= 1
            self.world['status'][(self.world['status'] == 1) & (self.world['timer'] < 0)] = 0
            self.history.append(lil_matrix(self.world['status']))
            death_tally = np.sum(self.world['status'] == 2)
            self.per.append(np.sum(self.world['status'] == 1) / (self.N * self.N - death_tally) * 100)
            self.death.append(death_tally / (self.N * self.N) * 100)
            t += dt

        # Animation
        cmap = ListedColormap(['white', 'red', 'black'])
        norm = BoundaryNorm([0, 1, 2, 3], cmap.N)
        fig = plt.figure(figsize=(12, 8))
        gs = GridSpec(1, 3, width_ratios =[6, 1, 1])
        ax1 = plt.subplot(gs[0])
        ax2 = plt.subplot(gs[1])
        ax3 = plt.subplot(gs[2])

        plot = ax1.imshow(self.history[0].toarray(), cmap=cmap, norm=norm)
        time_text = ax1.text(0.45, 1.05, '', transform=ax1.transAxes, color='black', fontsize=16)

        for ax in (ax1, ax2, ax3):
            ax.set_xticks([])
            ax.set_yticks([])

        infected_bar = ax2.bar(0, 100, color='red') # Setting initial width to 100
        diseased_bar = ax3.bar(0, 100, color='black') # Setting initial width to 100
        ax2.set_ylim(0, 100) # Change this line
        ax3.set_ylim(0, 100) # Change this line
        ax2.set_title('Infected (%)', fontsize=15)
        ax3.set_title('Diseased (%)', fontsize=15)

        def animate(i):
            plot.set_data(self.history[i].toarray())
            time_text.set_text('Day:  %.1f' % i)
            bar_inf = infected_bar[0]
            bar_dis = diseased_bar[0]
            bar_inf.set_height(self.per[i])
            bar_dis.set_height(self.death[i])
            return plot, time_text, bar_inf, bar_dis
        

        animation = FuncAnimation(fig,
                                  func=animate,
                                  frames=np.arange(len(self.history)),
                                  interval=150)
        html_animation = HTML(animation.to_jshtml())
        display(html_animation)
        plt.close()