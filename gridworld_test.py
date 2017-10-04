import unittest
from gridworld import GridWorld
from cell import Cell

class TestGridworld(unittest.TestCase):

    grid_world = None

    def setUp(self):
        global grid_world
        grid_world = GridWorld(world_size=2, infected_locations=[(1, 1)], prob_infect=0.5, prob_death=0.5, sick_day_range=[2, 6])

    def test_gridworld_initialization(self):
        global grid_world
        self.assertTrue(isinstance(grid_world.world[1][1], Cell))
        self.assertEqual(grid_world.world[1][1].health_status, 1)
        self.assertEqual(grid_world.world_size, 2)

    def test_get_neighbours(self):
        global grid_world
        self.assertEqual(len(grid_world.get_neighbours(grid_world.world[0][0])), 3)

    def test_get_world_map(self):
        global grid_world
        self.assertEqual(grid_world.get_world_map()[1][1].health_status, 1)

    def test_get_world_stats(self):
        global grid_world
        self.assertEqual(grid_world.get_world_stats()['total_healthy'], 3)


if __name__ == '__main__':
    unittest.main()