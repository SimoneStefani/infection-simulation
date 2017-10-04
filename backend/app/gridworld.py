#!/usr/bin/env python3
"""Representation of the world grid populated and relevant actions"""
__author__ = "Cedric Seger, Simone Stefani"
__copyright__ = "Copyright 2017, Cedric Seger and Simone Stefani"
__license__ = "MIT"

from cell import Cell


class GridWorld(object):
    def __init__(self, world_size, infected_locations, prob_infect, prob_death, sick_day_range):
        self.world_size = world_size
        self.world = self._init_world(world_size, infected_locations, prob_infect, prob_death, sick_day_range)

        # Statistics
        self.stats = {
            'daily_deaths': 0,
            'daily_recoveries': 0,
            'daily_infections': len(infected_locations),
            'total_cum_deaths': 0,
            'total_cum_infections': len(infected_locations),
            'total_cum_immune': 0,
            'total_healthy': self.world_size ** 2 - len(infected_locations),
            'total_sick': len(infected_locations)
        }

    # Create a N by N matrix and populate it with cell objects. Take care of
    # setting the infected cells.
    def _init_world(self, world_size, infected_locations, prob_infect, prob_death, sick_day_range):
        # Convert list to set (unless already done...)
        infected_locations = set(infected_locations)
        world_map = []
        for x in range(world_size):
            column = []
            for y in range(world_size):
                if (x, y) in infected_locations:
                    column.append(Cell((x, y), prob_infect, prob_death, sick_day_range, health_status=1))
                else:
                    column.append(Cell((x, y), prob_infect, prob_death, sick_day_range))

            world_map.append(column)

        return world_map

    # Advance the state of the world of one day. First loop through the cells
    # and spread the infection. Then compute the new state of each cell and
    # update the statistics of the world.
    def tick(self):
        # Spread disease
        for column in self.world:
            for cell in column:
                neighbours = self.get_neighbours(cell)
                cell.spread_disease(neighbours)

        # Update statuses and check deaths, recoveries etc (end of day)
        daily_infections = 0 # Number of individuals that became infected in a day (today) (i.e. recently infected)
        daily_deaths = 0 # Number of individuals that died in a day (today)
        daily_recoveries = 0 # Number of indv. that recovered in a day (today)
        total_sick = 0 # Number of ill individuals per day (i.e. total ill people in a day)
        # Assume that ill people refer to only ill cells and not recently_infected cells that are in incubation

        for column in self.world:
            for cell in column:
                state = cell.tick()

                if state == 1: # Cell got infected today
                    daily_infections += 1
                    #total_sick += 1
                elif state == 2: # Cell is just ill (but did not change state)
                    total_sick += 1
                elif state == 3: # Cell has died today
                    daily_deaths += 1
                elif state == -1: # Cell has recovered today
                    daily_recoveries += 1

        # Update global stats
        self.stats['daily_deaths'] = daily_deaths
        self.stats['daily_recoveries'] = daily_recoveries
        self.stats['daily_infections'] = daily_infections

        self.stats['total_cum_deaths'] += daily_deaths # once a cell is dead it cannot die again, just add
        self.stats['total_cum_infections'] += daily_infections
        self.stats['total_cum_immune'] += daily_recoveries

        self.stats['total_sick'] = total_sick
        self.stats['total_healthy'] = self.world_size ** 2 - self.stats['total_cum_infections']
        # Healthy is the same as not affected and hence population - affected = number of healthy

        return self.world

    # Determine the neighbours of a given cell.
    def get_neighbours(self, cell):
        x, y = cell.location

        offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        neighbours = []

        for i, j in offsets:
            if (x + i) in range(0, self.world_size) and (y + j) in range(0, self.world_size):
                neighbours.append(self.world[x + i][y + j])

        return neighbours

    # Return the world object as a N by N matrix containing cell objects.
    def get_world_map(self):
        return self.world

    # Return a dictionary with the statistics of the world.
    def get_world_stats(self):
        return self.stats
