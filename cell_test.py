import unittest
from cell import Cell

class TestCell(unittest.TestCase):

    cell = None

    def setUp(self):
        global cell
        cell = Cell(location=(3, 4), prob_infect=0.2, prob_death=0.6, sick_day_range=[3, 8], health_status=1)

    def test_get_status(self):
        global cell
        self.assertEqual(cell.get_status(), 1)

    def test_cell_string_form(self):
        global cell
        self.assertEqual(str(cell), "1")

    def test_cell_can_spread_disease_to_neighbour(self):
        cell = Cell((3, 4), 0.1, 0.6, [3, 8], 2) # Infected cell
        neighbour = Cell((3, 5), 1, 0.6, [3, 8], 0) # Healthy neighbour with prob_infect=1
        cell.spread_disease([neighbour])
        self.assertEqual(neighbour.get_status(), 1)

    def test_a_recently_infected_cell_cannot_spread_infection(self):
        cell = Cell((3, 4), 0.1, 0.6, [3, 8], 1) # Recently infected cell 
        neighbour = Cell((3, 5), 1, 0.6, [3, 8], 0) # Healthy neighbour with prob_infect=1
        cell.spread_disease([neighbour])
        self.assertEqual(neighbour.get_status(), 0)

    def test_a_sick_cell_cannot_be_infected(self):
        cell = Cell((3, 4), 0.1, 0.6, [3, 8], 2) # Sick cell
        cell.infect()
        self.assertEqual(cell.get_status(), 2)

    def test_an_immune_cell_cannot_be_infected(self):
        cell = Cell((3, 4), 0.1, 0.6, [3, 8], -1) # Immune cell
        cell.infect()
        self.assertEqual(cell.get_status(), -1)

    def test_a_cell_can_become_immune(self):
        global cell
        cell.days_to_immune = 0
        self.assertEqual(cell.tick(), -1)

    def test_a_just_infected_cell_becomes_sick(self):
        global cell
        cell.health_status = 1
        self.assertEqual(cell.tick(), 2)

    def test_a_sick_cell_may_die(self):
        global cell
        cell.health_status = 2
        cell.prob_death = 1
        self.assertEqual(cell.tick(), 3)
    

if __name__ == '__main__':
    unittest.main()