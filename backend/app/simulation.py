from gridworld import GridWorld
import util
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
	gridworld = GridWorld(args)
	# print(gridworld.get_world_map_values())
	ticks = 0
	while(gridworld.total_sick_count() > 0):
		gridworld.tick()
		print('Daily infections:{0}'.format(gridworld.get_daily_infections()))
		print('Total sick people {0}'.format(gridworld.total_sick_count()))
		ticks += 1
		print('tick..')
	print('FINISHED in {0} ticks!'.format(ticks))

	plt.imshow(gridworld.get_world_map_values())
	plt.colorbar()
	plt.show()

if __name__ == '__main__':
	args = util.parse_input()
	main(args)

