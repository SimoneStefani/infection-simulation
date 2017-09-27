import random

class Cell(object):

	def __init__(self, location, prob_infect, prob_death, sick_day_range, health_status=0):
		""" Object representing individual Cell in gridworld

			@args:
				location: Tuple representing board location
				health_status: Integer specifying status of Cell, default to healthy
					Possible Values:
						0 -> Healthy
						1 -> Recently infected
						2 -> Infected (normal)
						3 -> Dead
		"""
		self.random_days = lambda: random.randint(sick_day_range[0],sick_day_range[1])

		if health_status == 1:
			self.days_to_immune = self.random_days()
		else:
			self.days_to_immune = None # Replace with random number (consider removing)
		
		self.location = location # Tuple representing location --> Used for getting neighbours
		self.health_status = health_status # Healthy, immune, dead, ill, recently_infected
		self.prob_infect = prob_infect
		self.prob_death = prob_death

	def __str__(self):
		return str(self.health_status)

	def get_status(self):
		return self.health_status

	# Can only spread disease if infected (normal, status == 2)
	def spread_disease(self, neighbours):
		"""
		Cell tries to spread disease to neighbours
		Returns: Number of successfully infected neighbours
		"""
		number_of_infected = 0
		if self.health_status == 2: # Can spread disease
			for neighbour in neighbours:
				if neighbour.infect():
					number_of_infected += 1
		return number_of_infected

	def infect(self):
		""" Cell tries to infect its neighbour
			Returns: True if successful, else False
		"""
		# Possible to get infected -> healthy
		if self.health_status == 0:
			if random.uniform(0,1) < self.prob_infect:
				self.health_status = 1
				self.days_to_immune = self.random_days()
				return True

		return False

	def tick(self):
		if self.days_to_immune == 0:
			self.health_status = -1 # Immune
		elif self.health_status == 1:
			self.health_status = 2 # Infected (Normal)
		elif self.health_status == 2:
			if random.uniform(0,1) < self.prob_death:
				self.health_status = 3 # Dead
			else:
				# print(self.days_to_immune)
				# print(self.location)
				self.days_to_immune -= 1 # Immune







