from cell import Cell

class GridWorld(object):

	def __init__(self, settings):
		""" Object representing a square grid world/game world

			@args:
				world_size: Integer representing dimension of square grid world
				infected_locations: List of (tuple) locations of infected people
		"""

		self.world_size = settings.world_size 
		self.world = self._init_world(settings.world_size, settings.infected_locations,
			settings.chance_of_infection, settings.chance_of_death, settings.sick_days_min_max)

		# Stats
		self.daily_infected = 0

	def _init_world(self, world_size, infected_locations, prob_infect, prob_death, sick_day_range):
		infected_locations = set(infected_locations) # convert list to set (unless already done...)
		world_map = []
		for x in range(world_size):
			column = []
			for y in range(world_size):
				if (x,y) in infected_locations:
					column.append(Cell((x,y), prob_infect, prob_death, sick_day_range, health_status=1))
				else:
					column.append(Cell((x,y), prob_infect, prob_death, sick_day_range))

			world_map.append(column)

		return world_map

	def tick(self):
		# Spread disease
		daily_infections = 0
		for column in self.world:
			for cell in column:
				neighbours = self.get_neighbours(cell)
				num_infected = cell.spread_disease(neighbours)
				daily_infections += num_infected

		# Update statuses and check deaths etc (end of day)
		for column in self.world:
			for cell in column:
				cell.tick()


		# Update global stats (end of day)
		self.daily_infected = daily_infections

	def get_neighbours(self, cell):
		x,y = cell.location
		# print(cell.location)
		space = range(-1,2)
		# (x+i,y+j)
		neighbours = [self.world[x+i][y+j] for i in space for j in space if (x+i) in range(0,self.world_size) and (y+j) in range(0,self.world_size)]
		neighbours.remove(cell)
		return neighbours

	def get_world_map(self):
		return self.world

	def get_world_map_values(self):
		""" Returns a 2d list of cells' health status """
		return [list(map(lambda cell: cell.get_status(), column)) for column in self.world]

	# Private method not meant to be used outside of class
	def _count(self, status):
		count = 0
		status = set(status)
		for column in self.world:
			for cell in column:
				if cell.get_status() in status:
					count += 1
		return count

	# 0 -> Healthy
	# 1 -> Recently infected
	# 2 -> Infected (normal)
	# 3 -> Dead

	# COMBINE ALL THESE TO COUNT ALL STATUSes at end of day
	def total_sick_count(self):
		sick_count = self._count(status=[1,2])
		return sick_count

	def total_dead_count(self):
		sick_count = self._count(status=[3])
		return sick_count

	def total_healthy(self):
		sick_count = self._count(status=[0])
		return sick_count

	def get_daily_infections(self):
		return self.daily_infected



