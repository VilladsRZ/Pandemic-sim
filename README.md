# Pandemic-sim
This is a non deterministic simulator of how a disease (or any infectious mechanism) spreads in a population. Every individual has a unique healthscore emulating different factors such as imunesystem / age / illnesses that contribute to how susceptible they are to infection. Everyday, every invividual will interact with a random number of people within their socialsphere given the argument "daily_contact_rate". Additional to the individuals health, these encounters are subject to an additional element of randomness, emulating the different way people interact. The healthscore also changes the recovery time for each individual a little bit from the average so that healthier individuals recover faster.  <br> <br>
How to use: <br><br>
pip install requirements and download pandsim.py to folder <br><br>
import by running --> from pandsim import population <br><br>
See also examples. 
## Class Arguments

| Argument | Description |
| :--- | :--- |
| `N` | Sets the population size at $N \times N$. |
| `duration` | Sets the time for the simulation (in days). |
| `r_0` | Sets the initial population infection. |
| `infection_rate` | Sets the average chance for infection at encounter. |
| `mortality_rate` | Sets the chance for the individual to expire when infected. |
| `sociability` | Sets the social sphere of each person. Given by a $(1 + 2 \times \text{value}) \times (1 + 2 \times \text{value})$ matrix centered on the individual. |
| `daily_contact_rate` | Sets the percentage of contact within the given social sphere (where 1 is full contact). |
| `transmission_time` | Sets the amount of time an individual can transmit the disease after infection. |
| `imunity_time` | Sets the amount of time an individual is immune after recovery. |
