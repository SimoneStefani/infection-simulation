#!/usr/bin/env python3
"""Utility class for argument parsing in CL"""
__author__ = "Cedric Seger"
__copyright__ = "Copyright 2017, Cedric Seger and Simone Stefani"
__license__ = "MIT"

import argparse


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("--world_size", help="Size of population", type=int,
                        default=2, choices=range(2, 50))
    parser.add_argument('--infected_locations', nargs='+', type=int,
                        required=True, )
    parser.add_argument('--chance_of_infection', type=restricted_float,
                        default=0.50)
    parser.add_argument('--chance_of_death', type=restricted_float,
                        default=0.50)
    parser.add_argument('--sick_days_min_max', nargs='+', type=int,
                        default=[1, 6])
    args = parser.parse_args()

    check_day_range(args.sick_days_min_max)
    check_locations(args.infected_locations, args.world_size)

    # Zip input in form of 1 2 3 4 to coordinate tuples of form [(1,2), (3,4)]
    args.infected_locations = list(
        zip(args.infected_locations[0::2], args.infected_locations[1::2]))

    return args


# Ensure that the users specifies valid probability values.
def restricted_float(x):
    x = float(x)
    if x < 0.0 or x > 1.0:
        msg = '{} not in range [0.0, 1.0]'.format(x)
        raise argparse.ArgumentTypeError(msg)
    return x


# Ensure that the days specified by the users follow a logical order.
def check_day_range(day_range):
    if day_range[0] > day_range[1] or day_range[0] <= 0:
        msg = 'argument --sick_days_min_max: Specified range: {} does not follow format [min, max] where min > 0'.format(
            day_range)
        raise argparse.ArgumentTypeError(msg)


# Ensure that the locations input of the user are inside the
# boundaries of the GridWorld.
def check_locations(locations, world_size):
    if len(locations) % 2 != 0:
        msg = 'argument --locations: {} is not an even number of coordinates'.format(
            locations)
        raise argparse.ArgumentTypeError(msg)

    for coordinate in locations:
        if coordinate not in range(0, world_size + 1):
            msg = 'argument --locations: coordinate {0} must be in range [0,{1}]'.format(
                coordinate, world_size)
            raise argparse.ArgumentTypeError(msg)
