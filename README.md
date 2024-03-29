#### Royal Institute of Technology KTH - Stockholm
# Simulation of an Infectious Disease (II1304)

This small project consists in designing and experimenting with a simple model for a stochastic simulation on how an infectious disease could spread in a population. 

### How to get started?
1. Get a copy of this repository on your machine
```bash
git clone https://github.com/SimoneStefani/infection-simulation.git
cd infection-simulation
```

2. Set up virtual environment (highly suggested)
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the necessary libraries
```bash
pip3 install matplotlib
```


### Runnig the simulation

To run the simulation from command line execute the `simulate.py` file. This command accepts several arguments but only few are required:
* `infected_locations` (required), the positions of infected individuals
* `world_size` (required), the size of the population
* `chance_of_infection`, probability of an individual to get infected
* `chance_of_death`, probability of an individual of dying on a sick day
* `sick_days_min_max`, amount of days an individual can be sick
* `verbose` instructs the program to print statistical details for every day in the simulation and a final report

In order to run the simulation with default values:
```bash
python3 simulate.py --verbose
```

This is an example of how to run a simulation
```bash
python3 simulate.py --world_size 20 --infected_locations 4 5 --chance_of_infection 0.3 --chance_of_death 0.2 --sick_days_min_max 3 6 --verbose
```

### Runnig the test suite

This project contains a small test suite built using `unittest`. It can be run with:
```bash
python3 -m unittest discover . "*_test.py"
```
