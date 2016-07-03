'''I have noticed some funky stuff here... python 3 parses the file returns as
\n while python 2 uses \r this is not a trivial issue as it broke my program
at least once '''

_world = {}
starting_position = (0, 0)

def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()
        # print( 'with open rows',rows)
    x_max = len(rows[0].split('\t')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        # print( 'y: {0}, cols var: {1}'.format(y, cols))
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            # print( 'x: {0}, tile_name: {1}'.format(x,tile_name))
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))

if __name__ == '__main__':
    load_tiles()
    # print(_world)
