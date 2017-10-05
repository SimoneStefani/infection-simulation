from model import *
from util import parse_input
import matplotlib.pyplot as plt
import random
import statistics # Native python library (good)


def main(args):

    infection_prob_list = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    seed_list = [
        809, 863, 941, 1013, 1069, 1151, 1223, 1291, 1373, 1451, 1511, 1583, 1657, 1733,
        1811, 1889, 1987, 2053, 2129, 2213, 2287, 2357, 2423, 2531, 2617, 2687, 2741, 2819, 2903, 2999, 
        3079, 3181, 3257, 3331, 3413, 3511, 3571, 3643, 3727, 3821, 3907, 3989, 4057, 4139, 4231, 4297, 
        4409, 4493, 4583, 4657, 4751, 4831, 4937, 5003, 5087, 5179, 5279, 5387, 5443, 5521, 5639, 5693, 5791, 
        5857, 5939, 6053, 6133, 6221, 6301, 6367, 6473, 6571, 6673, 6761, 6833, 6917, 6997, 7103, 7207, 7297, 
        7411, 7499, 7561, 7643, 7723, 7829, 7919, 8017, 8111, 8219, 8291, 8387, 8501, 8597, 8677, 8741, 8831, 
        8929, 9011, 9109, 9199, 9283, 9377, 9439, 9533, 9631, 9733, 9811, 9887
        ]

    # Results to plot
    mean_total_affected = []
    std_total_affected = []

    population_size = args.world_size ** 2 # Total number of cells
    for infection_prob in infection_prob_list:
        print('Now calculating for prob: {}'.format(infection_prob))
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

    # Store raw results


    # Plot info here...
    plt.errorbar(infection_prob_list, mean_total_affected, yerr=std_total_affected, fmt='-o', label='num_affected')
    
    epidemic_line = [population_size/2 for i in range(len(infection_prob_list))]
    onehundred_line = [population_size for i in range(len(infection_prob_list))]

    plt.plot(infection_prob_list, epidemic_line, 'r--', label='Epidemic Line (50% infected)')
    plt.plot(infection_prob_list, onehundred_line, 'b--', label='100% infected')
    plt.axis([0, 1, -20, population_size+100])
    plt.xlabel('Probability of infecting a neighbor %')
    plt.ylabel('Number of infected cells')
    plt.title('Relationship between probability of infecting a neighbor and number of infected cells')
    plt.legend(loc='lower right')
    plt.show()


if __name__ == '__main__':
    args = parse_input()
    main(args)
