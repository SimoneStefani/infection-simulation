from .cell import Cell


# Object representing a square grid world/game world
class GridWorld(object):
    def __init__(self, world_size, infected_locations, prob_infect, prob_death, sick_day_range):
        self.world_size = world_size
        self.world = self._init_world(world_size, infected_locations, prob_infect, prob_death, sick_day_range)

        # Statistics
        self.stats = {
            'daily_deaths': 0,
            'daily_recoveries': 0,
            'daily_infections': len(infected_locations),
            'total_cum_deaths': 0,
            'total_cum_infections': len(infected_locations),
            'total_cum_immune': 0,
            'total_healthy': self.world_size ** 2 - len(infected_locations),
            'total_sick': len(infected_locations)
        }

    def _init_world(self, world_size, infected_locations, prob_infect, prob_death, sick_day_range):
        # Convert list to set (unless already done...)
        infected_locations = set(infected_locations)
        world_map = []
        for x in range(world_size):
            column = []
            for y in range(world_size):
                if (x, y) in infected_locations:
                    column.append(Cell((x, y), prob_infect, prob_death, sick_day_range, health_status=1))
                else:
                    column.append(Cell((x, y), prob_infect, prob_death, sick_day_range))

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
                    daily_recoveries += 1

        # Update global stats
        self.stats['daily_deaths'] = daily_deaths
        self.stats['daily_recoveries'] = daily_recoveries
        self.stats['daily_infections'] = daily_infections

        self.stats['total_cum_deaths'] += daily_deaths
        self.stats['total_cum_infections'] += daily_infections
        self.stats['total_cum_immune'] += daily_recoveries

        self.stats['total_healthy'] -= (daily_infections + daily_deaths - daily_recoveries)
        self.stats['total_sick'] += (daily_infections - daily_recoveries)

        return self.world

    def get_neighbours(self, cell):
        x, y = cell.location

        offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        neighbours = []

        for i, j in offsets:
            if (x + i) in range(0, self.world_size) and (y + j) in range(0, self.world_size):
                neighbours.append(self.world[x + i][y + j])

        return neighbours

    def get_world_map(self):
        return self.world

    def get_world_stats(self):
        return self.stats
