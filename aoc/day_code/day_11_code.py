from aoc.read import read_input
from aoc.utilities import time_wrap

from copy import deepcopy

_DAY = 11


def increase_step(data):
    """
    Adds 1 to every value in the data

    Parameters
    ----------
    data : list[list[int]]
        map of flash values

    Returns
    -------
    inc_data : list[list[int]]
        map of increased flash values

    """
    
    inc_data = data.copy()
    for row_idx, row in enumerate(data):
        for col_idx, col in enumerate(data):
            
            inc_data[row_idx][col_idx] = int(inc_data[row_idx][col_idx]) + 1
    
    return inc_data

def increase_neighbours(data, row, col):
    """
    Adds 1 to each neighbour which is on the grid

    Parameters
    ----------
    data : list[list[int]]
        map of flash values
    row : int
        row index of value to increment.
    col : int
        col index of value to increment.

    Returns
    -------
    data : list[list[int]]
        map of neighboured popped values

    """
    
    coords_to_increase = []
    
    #generate neighbour vlaues to add 1 to
    for rdelta in range(-1, 2, 1):
        for cdelta in range(-1, 2,1):
            neigh_row = row + rdelta
            neigh_col = col + cdelta
            
            #check on the grid
            if neigh_row >= 0 and neigh_row < len(data):
                if neigh_col >= 0 and neigh_col < len(data[0]):
                    coords_to_increase.append((neigh_row, neigh_col))
    
    #remove itself
    coords_to_increase.remove((row, col))
    
    #increment the popped locations
    for r, c in coords_to_increase:    
        data[r][c] += 1
        
    return data


def flash(data):
    """
    Performs a series of flashes - loops until nothing else has flashed
    - loops through all the data
    - if value is above 9 and the location hasn't flashed
    - checks to see if anything was added to the list of flashed values

    Parameters
    ----------
    data : list[list[int]]
        map of flash values

    Returns
    -------
    data : list[list[int]]
        map of resulting flash values
    len(flashed): int
        number of flashed values

    """
    
    flashed = []
    
    cont = True
    
    while cont: 
        temp_len = len(flashed)
        
        for row_idx, row in enumerate(data):
            for col_idx, value in enumerate(row):
                
                if value > 9 and (row_idx, col_idx) not in flashed:
                    data = increase_neighbours(data, row_idx, col_idx)
                    flashed.append((row_idx, col_idx))
                    
        if len(flashed) == temp_len:
            cont = False
                    
    return data, len(flashed)

def reset(data):
    """
    For each value in the data, sets anything above 9 equal to zero

    Parameters
    ----------
    data : list[list[int]]
        map of flash values

    Returns
    -------
    data : list[list[int]]
        map of resulting flash values

    """
    
    
    for row_idx, row in enumerate(data):
        reset_row = [c if c <= 9 else 0 for c in row]
        data[row_idx] = reset_row

    return data

def part_1(data, steps=100):
    """ Returns solution for part 1 """
    
    flash_count = 0
    for _ in range(steps):
       data = increase_step(data) 
       
       data, flash_temp = flash(data)
       
       flash_count += flash_temp
       
       data = reset(data)
    
    
    
    return flash_count
    
    
def part_2(data):
    """ Returns solution for part 2 """
    
    step = 1
    while True:
        step += 1
        data = increase_step(data)
        
        data, flash_temp = flash(data)
        
        data = reset(data)
        
        if flash_temp == 100:
            break
    
    return step

@time_wrap
def day():
    
    data = read_input(_DAY, test=False, extra_func=list)

    p1 = part_1(data)
    p2 = part_2(data)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()
