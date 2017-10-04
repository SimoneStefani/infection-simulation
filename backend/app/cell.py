#!/usr/bin/env python3
"""Representation of a cell (individual) and relevant actions"""
__author__ = "Cedric Seger, Simone Stefani"
__copyright__ = "Copyright 2017, Cedric Seger and Simone Stefani"
__license__ = "MIT"

import random


class Cell(object):
    def __init__(self, location, prob_infect, prob_death, sick_day_range, health_status=0):

        # limit range so that we cannot be sick for 0 days
        self.random_days = lambda: random.randint(sick_day_range[0], sick_day_range[1])

        if health_status == 1:
            self.days_to_immune = self.random_days()
        else:
            self.days_to_immune = None

        self.location = location  # Tuple representing location --> Used for getting neighbours
        self.health_status = health_status  # -1 = immune, 0 = healthy, 1 = just infected, 2 = sick 3 = dead
        self.prob_infect = prob_infect
        self.prob_death = prob_death

    # String representation of the cell
    def __str__(self):
        return str(self.health_status)

    # Get status of the cell
    def get_status(self):
        return self.health_status

    # Can only spread disease if infected (normal, status == 2)
    def spread_disease(self, neighbours):
        # Cell tries to spread disease to neighbours
        if self.health_status == 2:  # Can spread disease
            for neighbour in neighbours:
                neighbour.infect()

    def infect(self):
        # Cell tries to infect its neighbour
        # Possible to get infected -> healthy
        if self.health_status == 0:
            if random.uniform(0, 1) < self.prob_infect:
                self.health_status = 1
                self.days_to_immune = self.random_days()

    # Evaluate and advance state of a cell
    # Only returns a value if there has been a change in the health_status of a cell
    def tick(self):
        if self.days_to_immune == 0: # Zero days left to recovery
            self.health_status = -1  # Cell becomes immune
            self.days_to_immune = None # Reset so that immune cell is not double counted
            return -1

        elif self.health_status == 1: # Recently_infected turns into ill cell
            self.health_status = 2  # Ill cell
            return 1

        elif self.health_status == 2: # Cell is ill
            if random.uniform(0, 1) < self.prob_death:
                self.health_status = 3  # Cell dies
                return 3
            else:
                # print(self.days_to_immune)
                # print(self.location)
                self.days_to_immune -= 1  # Immune
                #return None  # No information to udpate

        # A cell that is healthy or immune or dead return none (no state change)
        # Also a cell that is ill but does not die returns none (no state change)





