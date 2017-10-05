from model import *
from util import parse_input
# import matplotlib.pyplot as plt


def main(args):

    healthy = []
    sick = []
    dead = []
    immune = []
    total_incubated = [] # recently infected, in incubation period
    ticks = 0

    create_world(args.world_size, args.infected_locations, args.chance_of_infection, args.chance_of_death, args.sick_days_min_max)

    # Run Simulation till end
    while True:
        tick_world()

        ticks += 1
        stats = get_world_stats() # Represent end of day stats

        if (args.verbose):
            print('Statistics for day {}'.format(ticks))
            print('-'*40)
            print_statistics()
            print()

        # The 5 possible categories for cell state (should add to 100%)
        sick.append(stats['total_sick'])
        dead.append(stats['total_cum_deaths'])
        healthy.append(stats['total_healthy'])
        immune.append(stats['total_cum_immune'])
        total_incubated.append(stats['daily_infections'])

        if stats['total_sick'] == 0 and stats['daily_infections'] == 0:
            break

    if (args.verbose):
        # Print final results
        print('Finished simulation in {0} ticks'.format(ticks))
        print('Final outcome statistics:')
        print('-'*40)
        print('Total number of healthy individuals: {0}'.format(healthy[-1]))
        print('Total number of dead individuals: {0}'.format(dead[-1]))
        print('Total number of immune individuals: {0}'.format(immune[-1]))
        print('Total number of ill individuals: {0}'.format(sick[-1]))
        print('Total number of individuals in incubation period: {0}'.format(total_incubated[-1]))
        print('(Initial Population of healthy individuals: {})'.format(args.world_size ** 2))
        print()

        # Plot Results
        # plt.plot(range(ticks), sick, 'ro', label='Sick')
        # plt.plot(healthy, 'bo', label='Healthy')
        # plt.plot(dead, 'go', label='Dead')
        # plt.plot(immune, 'o', label='Immune')
        # plt.plot(total_incubated, 'o', label='Incubated')
        # plt.xlabel('Duration of simulation in days')
        # plt.ylabel('Number of cells')
        # plt.title('Dynamics of disease spreding in terms of cells status')
        # plt.legend(loc='upper right')
        # plt.show()


if __name__ == '__main__':
    args = parse_input()
    main(args)
