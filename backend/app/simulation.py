from .gridworld import GridWorld
from .util import parse_input
import matplotlib.pyplot as plt

# Global instance of GridWorld. It is used by the client in order
# to tick every time the same instance of the GridWorld.
grid_world = None


# Generate a global instance of GridWorld. This function is mainly
# used by the JavaScript client when the user press play.
def generate_world():
    global grid_world
    grid_world = GridWorld({
        "world_size": 40,
        "infected_locations": [(5, 20), (35, 4)],
        "sick_days_min_max": [1, 6],
        "chance_of_death": 0.5,
        "chance_of_infection": 0.5
    })


# Advance the simulation on the global instance of GridWorld of
# one step. Return the new configuration of GridWorld.
def tick_simulation():
    global grid_world
    grid_world.tick()
    return grid_world.get_world_map_values()


def main(args):
    grid_world = GridWorld(args)
    ticks = 0

    while True:
        sick_count = grid_world.tick()
        ticks += 1
        print('tick..')
        if sick_count <= 0:
            break

    print('FINISHED in {0} ticks!'.format(ticks))

    plt.imshow(grid_world.get_world_map_values())
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    args = parse_input()
    main(args)
