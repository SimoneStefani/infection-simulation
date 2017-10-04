from model import *
from util import parse_input
import matplotlib.pyplot as plt
import random
import statistics # Native python library (good)


def main(args):

    infection_prob_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    seed_list = [613, 383, 409, 113, 911, 859, 967]

    # Results to plot
    mean_total_affected = []
    std_total_affected = []

    population_size = args.world_size ** 2 # Total number of cells
    for infection_prob in infection_prob_list:
        # Statistics at the end of each simulation
        total_affected = [] # How many cells got infected
        for seed in seed_list:
            # Set the seed for this simulation
            # Another solution would simply be to just run 100 trials and not reset seed
            random.seed(seed)
            # Create a world, might want to randomize starting positions automatically?
            create_world(args.world_size, args.infected_locations, infection_prob, args.chance_of_death, args.sick_days_min_max)
            total_ticks = 0
            stats = None
            # Simulate until stopping condition
            while True:
                tick_world()
                total_ticks += 1
                stats = get_world_stats()
                if stats['total_sick'] == 0 and stats['daily_infections'] == 0:
                    break
            reset_world() # Might not be necessary?
            # Add stats for this seed
            #total_affected.append(population_size - stats['total_healthy'])
            total_affected.append(stats['total_cum_infections'])
            # Cell has five states, at the end of a simulation cells can only have 3
            # possible states: Healthy (unaffected), Dead or Immune. If cells are not
            # healthy, then they must have been infected at some point.

        # Calculate mean and stds from raw results here...
        # Append as dictionary to results (prob: affected_people)
        mean_total_affected.append(statistics.mean(total_affected))
        std_total_affected.append(statistics.stdev(total_affected))
        # print(statistics.stdev(total_affected))
        # print('Mean is: {0}'.format(statistics.mean(total_affected)))


    # Plot info here...
    plt.errorbar(infection_prob_list, mean_total_affected, yerr=std_total_affected, fmt='-o', label='num_affected')
    
    epidemic_line = [population_size/2 for i in range(len(infection_prob_list))]
    onehundred_line = [population_size for i in range(len(infection_prob_list))]

    plt.plot(infection_prob_list, epidemic_line, 'r--', label='Epidemic Line (50% infected)')
    plt.plot(infection_prob_list, onehundred_line, 'b--', label='100% infected')
    plt.axis([0, 1, -20, population_size+100])
    plt.xlabel('Probability of infecting %')
    plt.ylabel('Number of affected cells')
    plt.title('Prob. infect vs. num_affected cells')
    plt.legend(loc='center right')
    plt.show()


if __name__ == '__main__':
    args = parse_input()
    main(args)
