from .gridworld import GridWorld
import argparse
import matplotlib.pyplot as plt

# import matplotlib.animation as animation

# gridworld = GridWorld(world_size=15, infected_locations=[(0,0)])

# print(gridworld.get_world_map_values())
# ticks = 0
# while(gridworld.count([1,2])):
# 	gridworld.tick()
# 	ticks += 1
# 	print('tick..')
# print('FINISHED in {0} ticks!'.format(ticks))
# print(gridworld.get_world_map_values())

# plt.imshow(gridworld.get_world_map_values())
# plt.colorbar()
# plt.show()

gridworld = None

def go(args):
	gridworld = GridWorld(world_size=args.N, infected_locations=[(0,0)])
	print(gridworld.get_world_map_values())
	ticks = 0
	while(gridworld.count([1,2])):
		gridworld.tick()
		ticks += 1
		print('tick..')
	print('FINISHED in {0} ticks!'.format(ticks))
	print(gridworld.get_world_map_values())

	plt.imshow(gridworld.get_world_map_values())
	plt.colorbar()
	plt.show()

def genWorld():
	global gridworld 
	gridworld = GridWorld(world_size=50, infected_locations=[(5,20), (35,4)])

def tickSim():
	global gridworld
	gridworld.tick()
	return gridworld.get_world_map_values()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--N", help="Size of population", type=int, default=2, choices=range(0,20))
	args = parser.parse_args()
	
	go(args)


if __name__ == '__main__':
	print('Running script...\n')
	main()

