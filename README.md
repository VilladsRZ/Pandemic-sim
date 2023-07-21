# Pandemic-sim
This is a simulator of how a disease (or any infectious mechanisms) spreads in a population. Below are the following class arguments. <br> <br>
N                  --> sets the population size at N*N. <br>
duration           --> sets the time for the simulation (in days). <br>
r_0                --> sets the initial population infection. <br>
infection_rate     --> sets the average chance for infection at encounter. <br>
mortality_rate:    --> sets the chance for the individual to expire at when infected. <br>
sociability:       --> sets the interaction-sphere of each person. Is given by a (1 + 2 x value) x (1 + 2 x value) matrix centered on the individual.
transmission_time  --> sets the amount of time an individual can transmit the disease after infection. <br>
imunity_time       --> sets the amount of time of an individual is imune after recovery. <br>
