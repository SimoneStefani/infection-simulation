from gridworld import GridWorld

grid_world = None


def create_world(world_size, infected_locations, prob_infect, prob_death, sick_day_range):
    global grid_world
    grid_world = GridWorld(world_size, infected_locations, prob_infect, prob_death, sick_day_range)


def tick_world():
    global grid_world
    grid_world.tick()


def reset_world():
    global grid_world
    grid_world = None


def get_world_representation():
    global grid_world
    world = grid_world.get_world_map()
    return [list(map(lambda cell: cell.get_status(), column)) for column in world]


def get_world_stats():
    global grid_world
    return grid_world.get_world_stats()


def print_statistics():
    stats = get_world_stats()

    print('Daily deaths: {0}'.format(stats['daily_deaths']))
    print('Daily recoveries: {0}'.format(stats['daily_recoveries']))
    print('Daily infections: {0}'.format(stats['daily_infections']))
    print('-' * 40)
    print('Total sick people: {0}'.format(stats['total_sick']))
    print('Total healthy people: {0}'.format(stats['total_healthy']))
    print('Total dead people: {0}'.format(stats['total_cum_deaths']))
    print('Total immune people: {0}'.format(stats['total_cum_immune']))
    print()
