#!/usr/bin/env python3
"""Public API to the infectious disease simulation components"""
__author__ = "Simone Stefani"
__copyright__ = "Copyright 2017, Cedric Seger and Simone Stefani"
__license__ = "MIT"

from gridworld import GridWorld

grid_world = None

# Create a new world grid populated with individuals.
# Arguments:    world_size -- the number N which generates a world of size N x N
#               infected_locations -- a list of tuples with coordinates of infected individuals
#               prob_infect -- the probability that an individual will infect one neighbour
#               prob_death -- the probability that an infected individual would die on a given day
#               sick_day_range - min and max days an individual can be sick
def create_world(world_size, infected_locations, prob_infect, prob_death, sick_day_range):
    global grid_world
    grid_world = GridWorld(world_size, infected_locations, prob_infect, prob_death, sick_day_range)


# Advance the state of the world (population) of one day.
def tick_world():
    global grid_world
    grid_world.tick()


# Reset the current instance of the world grid to its initial state.
def reset_world():
    global grid_world
    grid_world = None


# Get a two-dimensional matrix representation of the world grid.
# Returns:      two-dimensional matrix containing the states of the individuals
#                   -1 = immune
#                   0 = healthy
#                   1 = just infected (on the same day)
#                   2 = sick
#                   3 = dead
def get_world_representation():
    global grid_world
    world = grid_world.get_world_map()
    return [list(map(lambda cell: cell.get_status(), column)) for column in world]


# Get statistical data on the simulation based on the current day.
# Returns:      dictionary with statistical data
#                   daily_deaths = deaths during the current day
#                   daily_recoveries = individuals become immune during the current day
#                   daily_infections = individual infected during the current day
#                   total_sick = total amount of individuals sick on the current day
#                   total_healthy = total amount of individuals healthy or immune on the current day
#                   total_cum_deaths = total deaths up to current day
#                   total_cum_immune = total immune up to current day
def get_world_stats():
    global grid_world
    return grid_world.get_world_stats()


# Print in command line the statistics of the current day.
def print_statistics():
    stats = get_world_stats()
    print('Daily infections: {0}'.format(stats['daily_infections']))
    print('Daily deaths: {0}'.format(stats['daily_deaths']))
    print('Daily recoveries: {0}'.format(stats['daily_recoveries']))
    print('Total number of ill people: {0}'.format(stats['total_sick']))
    print('Total cumulative infections: {0}'.format(stats['total_cum_infections']))
    print('Total cumulative deaths: {0}'.format(stats['total_cum_deaths']))
    print()
    
    
    
