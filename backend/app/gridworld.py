from cell import Cell

class GridWorld(object):

	def __init__(self, settings):
		""" Object representing a square grid world/game world
		"""

		self.world_size = settings.world_size 
		self.world = self._init_world(settings.world_size, settings.infected_locations,
			settings.chance_of_infection, settings.chance_of_death, settings.sick_days_min_max)

		# STATS
		self.stats = {
			'daily_deaths': 0,
			'daily_recoveries': 0,
			'daily_infections': 0,
			'total_cum_deaths': 0,
			'total_cum_infections': 0,
			'total_cum_immune': 0,
			'total_healthy': self.world_size ** 2,
			'total_sick': 0
		}

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
		for column in self.world:
			for cell in column:
				neighbours = self.get_neighbours(cell)
				cell.spread_disease(neighbours)

		# Update statuses and check deaths, recoveries etc (end of day)
		daily_infections = 0
		daily_deaths = 0
		daily_recoveries = 0
		for column in self.world:
			for cell in column:
				information = cell.tick()

				if information == 1:
					daily_infections += 1
				elif information == 3:
					daily_deaths += 1
				elif information == -1:
					daily_recoveries =+ 1

		# Update global stats
		self.stats['daily_deaths'] = daily_deaths
		self.stats['daily_recoveries'] = daily_recoveries
		self.stats['daily_infections'] = daily_infections

		self.stats['total_cum_deaths'] += daily_deaths
		self.stats['total_cum_infections'] += daily_infections
		self.stats['total_cum_immune'] += daily_recoveries

		self.stats['total_healthy'] -= daily_infections # Prevent to go below zero...?
		not_sick_count = self.stats['total_healthy'] + self.stats['total_cum_deaths'] + self.stats['total_cum_immune']
		self.stats['total_sick'] = (self.world_size**2) - not_sick_count
		
		# Print stats
		print('Daily deaths: {0}'.format(self.stats['daily_deaths']))
		print('Daily recoveries: {0}'.format(self.stats['daily_recoveries']))
		print('Daily infections: {0}'.format(self.stats['daily_infections']))
		print('-'*20)
		print('Total sick people: {0}'.format(self.stats['total_sick']))
		print('Total healthy people: {0}'.format(self.stats['total_healthy']))
		print('Total dead people: {0}'.format(self.stats['total_cum_deaths']))
		print('Total immune people: {0}'.format(self.stats['total_cum_immune']))
		print()

		return self.stats['total_sick']

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

