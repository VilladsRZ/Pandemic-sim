# Pandemic-sim
This is a non deterministic simulator of how a disease (or any infectious mechanisms) spreads in a population. Every individual has a unique healthscore emulating different factor such as imunesystem / age / diseases that indicates how susceptible they are to infection. Everyday, every invividual will interact with a random number of people within their socialsphere given the argument "daily_contact_rate". Additional to the individuals health, all encounters include a random interaction factor for the infection chance, emulating the different way people interact.  <br> <br>
import by running --> from pandsim import population <br>
Below are the following class arguments.
N                  --> sets the population size at N*N. <br>
duration           --> sets the time for the simulation (in days). <br>
r_0                --> sets the initial population infection. <br>
infection_rate     --> sets the average chance for infection at encounter. <br>
mortality_rate:    --> sets the chance for the individual to expire at when infected. <br>
sociability:       --> sets the interaction-sphere of each person. Is given by a (1 + 2 x value) x (1 + 2 x value) matrix centered on the individual. <br>
daily_contact_rate --> sets the procentage of contact within the given socialsphere, where 1 is full contact. 
transmission_time  --> sets the amount of time an individual can transmit the disease after infection. <br>
imunity_time       --> sets the amount of time of an individual is imune after recovery. <br>
