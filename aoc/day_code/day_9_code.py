from aoc.read import read_input
from aoc.utilities import time_wrap

import re

_DAY = 9

def fit_test(data, row, col, row_delta, col_delta):
    
    minimum = False
    
    test_row = row + row_delta
    test_col = col + col_delta
    
    if test_row >= 0 and test_row < len(data):
        if test_col >= 0 and test_col < len(data[0]):
            if data[row][col] < data[row + row_delta][col + col_delta]:
                minimum = True
        else:
            minimum = True
    else:
        minimum = True
        
    return minimum


def local_min(data, row_idx, col):
    
    minimum = False
    
    if fit_test(data, row_idx, col, -1, 0):
        if fit_test(data, row_idx, col, 1, 0):
            if fit_test(data, row_idx, col, 0, -1):
                if fit_test(data, row_idx, col, 0, 1):
                    minimum = True
    
    return minimum
        

def part_1(data, coords=False):
    """ Returns solution for part 2 """
    
    mins = []
    locations = []
    for row_idx, row in enumerate(data):
        for col in range(len(row)):
            
            if local_min(data, row_idx, col):
                mins.append(data[row_idx][col])
                locations.append((row_idx, col))
    
    


    mins = [int(v) for v in mins]
    risk_levels = sum(mins) + len(mins)
    
    if coords:
        return risk_levels, locations
    else:
        return risk_levels
    
    

def valid_neighbour(current, delta, basin_map, _peak=9):
    """
    Tests if a neighbouring cell is valid, ie not off the edge of the map, and 
    not a peak (9), and returns the cell coords if all fine

    Parameters
    ----------
    current : tuple(int, itn)
        Current location to test valid neighbour for.
    delta : tuple(int, int)
        Specific neighbour delta from current.
    basin_map : list[list[str]]
        Original source map.
    _peak : int 
        Height of basin peaks. The default is 9

    Returns
    -------
    valid_neighbour : tuple(int, int) 
        Returns neighbour coord if valid, otherwise None.

    """
    
    valid_neighbour = None
    
    row = current[0] + delta[0]
    col = current[1] + delta[1]
    
    if row >= 0 and row < len(basin_map):
        if col >= 0 and col < len(basin_map[0]):
            #exists in map
            if int(basin_map[row][col]) < _peak:
                valid_neighbour = (row, col)
                
    return valid_neighbour

    
def find_neighbours(current, basin_map):
    """
    For the current cell, finds all neighbours which are valid and returns them
    as a list of coords

    Parameters
    ----------
    current : tuple(int, itn)
        Current location to test valid neighbour for.
    basin_map : list[list[str]]
        Original source map.

    Returns
    -------
    neighbours : list[tuple(int, int)]
        DESCRIPTION.

    """
    
    directions = []
    neighbours = []
        
    for val in range(-1, 2, 2): #deltas for neighbouring cells
        directions.append((val, 0))
        directions.append((0, val))
        
    for delta in directions:
        valid = valid_neighbour(current, delta, basin_map)
        if valid:
            neighbours.append(valid)
    
    
    
    return neighbours
  

def multiply(values):
    """ multiplies collection of values together """
    
    mult = 1
    
    for v in values:
        mult *= v
        
    return mult
    
    
def part_2(data, locations):
    """
    Loops through minimum points, builds up neighbouring networks of unreached
    tiles where neighbours are valid and not peaks, then multiplies largest 3 
    for the answer to day 9 part 2    

    Parameters
    ----------
    data : list[list[str]]
        Original source map.
    locations :  list[tuple(coord, coord)]
        List of minimum points in map from part 1

    Returns
    -------
    int
        sizes of largest 3 basins multipled together.

    """
    
    # all basins have a single low point - so 1 basin per minimum location 
    # found in part 1
    # all basins flow downhill - so can stop looking if find a level 8 value
    
    
    basin_sizes = []
    
    for minimum in locations: 
        #for each basin, new frontier
        #frontier is edge cells yet to be explored
        frontier = []
        frontier.append(minimum)
        
        #reached is cells that have been touched upon
        reached = {}
        reached[minimum] = True
        
        while len(frontier) > 0: #still more to discover
            current = frontier.pop(0)
            
            for neighbour in find_neighbours(current, data):
                if neighbour not in reached:
                    #new cell to explore, and add to finished list
                    frontier.append(neighbour)
                    reached[neighbour] = True
                        
        basin_sizes.append(len(reached))

    #return largest 3 basins multipled
    return multiply(sorted(basin_sizes)[-3:])


@time_wrap
def day():
    
    data = read_input(_DAY, test=False, extra_func=list)

    p1, locations = part_1(data, coords=True)
    p2 = part_2(data, locations)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()