from model import *
from util import parse_input
import matplotlib.pyplot as plt


def main(args):

    healthy = []
    sick = []
    dead = []
    # cum_dead = []
    immune = []
    total_incubated = [] # recently infected, in incubation period
    ticks = 0

    create_world(args.world_size, args.infected_locations, args.chance_of_infection, args.chance_of_death, args.sick_days_min_max)

    while True:
        tick_world()

        ticks += 1
        stats = get_world_stats() # Represent end of day stats

        # The 5 possible categories for cell state (should add to 100%)
        sick.append(stats['total_sick'])
        dead.append(stats['total_cum_deaths'])
        healthy.append(stats['total_healthy'])
        immune.append(stats['total_cum_immune'])
        total_incubated.append(stats['daily_infections'])

        if stats['total_sick'] == 0 and stats['daily_infections'] == 0:
            break

    print('FINISHED in {0} ticks!'.format(ticks))

    plt.plot(range(ticks), sick, 'ro', label='Sick')
    plt.plot(healthy, 'bo', label='Healthy')
    plt.plot(dead, 'go', label='Dead')
    plt.plot(immune, 'o', label='Immune')
    plt.plot(total_incubated, 'o', label='Incubated')


    plt.legend(loc='upper right')

    plt.show()


if __name__ == '__main__':
    args = parse_input()
    main(args)
