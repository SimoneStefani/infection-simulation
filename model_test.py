import unittest
from model import *


class TestModel(unittest.TestCase):

    # In a world with chance of infection 0 and chance of death 1
    # the infected individual dies before spreading the disease
    def test_world_with_max_death_min_infection(self):
        create_world(world_size=2, infected_locations=[(1, 1)], prob_infect=0, prob_death=1, sick_day_range=[2, 6])

        while True:
            tick_world()
            stats = get_world_stats()
            if stats['total_sick'] == 0 and stats['daily_infections'] == 0:
                break

        self.assertEqual(get_world_stats()['total_cum_deaths'], 1)
        self.assertEqual(get_world_stats()['total_sick'], 0)
        self.assertEqual(get_world_stats()['daily_infections'], 0)


    # In a world with chance of infection 1 and chance of death 0
    # all the individuals will eventually become immune
    def test_world_with_min_death_max_infection(self):
        create_world(world_size=2, infected_locations=[(1, 1)], prob_infect=1, prob_death=0, sick_day_range=[2, 6])

        while True:
            tick_world()
            stats = get_world_stats()
            if stats['total_sick'] == 0 and stats['daily_infections'] == 0:
                break

        self.assertEqual(get_world_stats()['total_cum_deaths'], 0)
        self.assertEqual(get_world_stats()['total_cum_immune'], 4)

    
    # Check that at the end of a random simulation the number of
    # deaths + immunes + healthy adds up to the total number of individuals
    def test_correct_sum_states_at_end_of_simulation(self):
        create_world(world_size=20, infected_locations=[(1, 1)], prob_infect=0.5, prob_death=0.5, sick_day_range=[2, 6])

        while True:
            tick_world()
            stats = get_world_stats()
            if stats['total_sick'] == 0 and stats['daily_infections'] == 0:
                break

        print(get_world_representation())
        stats = get_world_stats()
        sum_states = stats['total_cum_deaths'] + stats['total_cum_immune']
        self.assertEqual(sum_states, 20*20)


if __name__ == '__main__':
    unittest.main()