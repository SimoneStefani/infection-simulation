from model import *
from util import parse_input
import matplotlib.pyplot as plt


def main(args):

    healthy = []
    sick = []
    dead = []
    cum_dead = []
    ticks = 0

    create_world(args.world_size, args.infected_locations, args.chance_of_infection, args.chance_of_death, args.sick_days_min_max)

    while True:
        tick_world()

        ticks += 1
        stats = get_world_stats() # Represent end of day stats

        healthy.append(stats['total_healthy'])
        sick.append(stats['total_sick'])
        dead.append(stats['total_cum_deaths'])
        cum_dead.append(stats['total_cum_deaths'])

        if stats['total_sick'] == 0 and stats['daily_infections']:
            break

    print('FINISHED in {0} ticks!'.format(ticks))

    plt.plot(range(ticks), sick, 'ro', label='Sick')
    plt.plot(healthy, 'bo', label='Healthy')
    plt.plot(cum_dead, 'go', label='Dead')
    plt.legend(loc='center right')

    plt.show()


if __name__ == '__main__':
    args = parse_input()
    main(args)
