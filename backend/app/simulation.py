from gridworld import GridWorld
import argparse
import matplotlib.pyplot as plt

gridworld = None

def genWorld():
	global gridworld 
	gridworld = GridWorld(world_size=50, infected_locations=[(5,20), (35,4)])

def tickSim():
	global gridworld
	gridworld.tick()
	return gridworld.get_world_map_values()


def main(args):
	starting_locations = list(zip(args.locations[0::2], args.locations[1::2]))
	
	gridworld = GridWorld(world_size=args.n, infected_locations=starting_locations)
	# print(gridworld.get_world_map_values())
	ticks = 0
	while(gridworld.count([1,2])):
		gridworld.tick()
		ticks += 1
		print('tick..')
	print('FINISHED in {0} ticks!'.format(ticks))
	# print(gridworld.get_world_map_values())

	plt.imshow(gridworld.get_world_map_values())
	plt.colorbar()
	plt.show()


def restricted_float(x):
	x = float(x)
	if x < 0.0 or x > 1.0:
		msg = '{} not in range [0.0, 1.0]'.format(x)
		raise argparse.ArgumentTypeError(msg)
	return x

def check_day_range(day_range):
	if day_range[0] > day_range[1]:
		msg = 'argument --sick_days_min_max: Specified range: {} does not follow format [min, max]'.format(day_range)
		raise argparse.ArgumentTypeError(msg)

def check_locations(locations, world_size):
	if len(locations) % 2 != 0:
		msg = 'argument --locations: {} is not an even number of coordinates'.format(locations)
		raise argparse.ArgumentTypeError(msg)
	
	for coordinate in locations:
		if coordinate not in range(0,world_size+1):
			msg = 'argument --locations: coordinate {0} must be in range [0,{1}]'.format(coordinate, world_size)
			raise argparse.ArgumentTypeError(msg)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("--n", help="Size of population", type=int, default=2, choices=range(2,20))
	parser.add_argument('--locations', nargs='+', type=int, required=True)
	parser.add_argument('--chance_of_infection', type=restricted_float, default=0.50)
	parser.add_argument('--chance_of_death', type=restricted_float, default=0.50)
	parser.add_argument('--sick_days_min_max', nargs='+', type=int, default=[1, 6])
	args = parser.parse_args()

	check_day_range(args.sick_days_min_max)
	check_locations(args.locations, args.n)

	main(args)

