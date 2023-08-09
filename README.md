# Pandemic-sim
This is a non deterministic simulator of how a disease (or any infectious mechanisms) spreads in a population. Every individual has a unique healthscore emulating different factors such as imunesystem / age / illnesses that contribute to how susceptible they are to infection. Everyday, every invividual will interact with a random number of people within their socialsphere given the argument "daily_contact_rate". Additional to the individuals health, these encounters are subject to an additional element of randomness, emulating the different way people interact. The healthscore also changes the recovery time for each individual a little bit from the average so that healthier individuals recover faster.  <br> <br>
import by running --> from pandsim import population <br><br>
Below are the following class arguments. <br><br>
N                  --> sets the population size at N*N. <br>
duration           --> sets the time for the simulation (in days). <br>
r_0                --> sets the initial population infection. <br>
infection_rate     --> sets the average chance for infection at encounter. <br>
mortality_rate:    --> sets the chance for the individual to expire at when infected. <br>
sociability:       --> sets the interaction-sphere of each person. Is given by a (1 + 2 x value) x (1 + 2 x value) matrix centered on the individual. <br>
daily_contact_rate --> sets the procentage of contact within the given socialsphere, where 1 is full contact. 
transmission_time  --> sets the amount of time an individual can transmit the disease after infection. <br>
imunity_time       --> sets the amount of time of an individual is imune after recovery. <br>
