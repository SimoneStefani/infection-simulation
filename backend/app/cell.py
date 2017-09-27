
#Should inherit from mother class with:
# Prob. to infect
# Days ill function (min,max) uniform
# Prob. of dying
# Get neighbours function w. input = location
# Specify possible health_statuses --> Used for testing/checking correct health status


# -1 -> Immune
# 0 -> Alive
# 1 -> Recently infected
# 2 -> Infected (Normal)
# 3 -> Dead

import random
class Cell(object):

	def __init__(self, location, health_status=0):
		""" Object representing individual Cell in gridworld

			@args:
				location: Tuple representing board location
				health_status: Integer specifying status of Cell, default to healthy

		"""
		if health_status == 1:
			self.days_to_immune = random.randint(1,4)
		else:
			self.days_to_immune = None # Replace with random number (consider removing)
		
		self.location = location # Tuple representing location --> Used for getting neighbours
		self.health_status = health_status # Healthy, immune, dead, ill, recently_infected

	def __str__(self):
		return str(self.health_status)

	def get_status(self):
		return self.health_status

	# Can only spread disease if infected (normal, status == 2)
	def spread_disease(self, neighbours):
		if self.health_status == 2: # Can spread disease
			for neighbour in neighbours:
				neighbour.infect()

	def infect(self):
		# Possible to get infected -> healthy
		if self.health_status == 0:
			if random.uniform(0,1) > 0.50: # change later
				self.health_status = 1
				self.days_to_immune = random.randint(3,4) # change later

	def tick(self):
		if self.days_to_immune == 0:
			self.health_status = -1 # Immune
		elif self.health_status == 1:
			self.health_status = 2 # Infected (Normal)
		elif self.health_status == 2:
			if random.uniform(0,1) > 0.50:
				self.health_status = 3 # Dead
			else:
				# print(self.days_to_immune)
				# print(self.location)
				self.days_to_immune -= 1 # Immune







