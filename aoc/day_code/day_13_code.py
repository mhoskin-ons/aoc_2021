from aoc.read import read_input
from aoc.utilities import time_wrap

import pandas as pd

_DAY = 13

_VALS = {'x':0, 
         'y':1}

def split_data(data):
    
    split = data.index('')
    
    points = data[:split]
    points = [tuple(p.split(',')) for p in points]
    
    folds = data[split+1:]
    folds = [f.split(' ')[-1] for f in folds]
    folds = [f.split('=') for f in folds]
    
    return points, folds
  

def fold(points, axis, value):
    
    fold_idx = _VALS[axis]
    
    for point_idx, point in enumerate(points):
        if int(point[fold_idx]) > value:
            temp_point = list(point)
            temp_point[fold_idx] = str(2 * value - int(temp_point[fold_idx]))
            
            points[point_idx] = tuple(temp_point)
            
    points = list(set(points))
    
    return points

def part_1(points, folds):
    """ Returns solution for part 1 """
    
    lengths = []
    lengths.append(len(points))
    for step in folds:
        axis = step[0]
        value = int(step[1])
             
        points = fold(points, axis, value)
        lengths.append(len(points))
    
    
    return lengths[1], points
    
   
def display(points):
    
    table = pd.DataFrame(points)
    
    table[0] = pd.to_numeric(table[0])
    table[1] = pd.to_numeric(table[1])
    
    table.plot(x=0, y=1, kind='scatter',
               ylim=[3*max(table[1]), -max(table[1])])
    
def part_2(points):
    """ Returns solution for part 2 """
    
    display(points)
    
    max_x = max(int(p[0]) for p in points)
    max_y = max(int(p[1]) for p in points)
    
    #grid doesn't work for some reason, despite the results of grid and grid2
    #being identical 
    grid = [[' '] * (max_x+1)]*(max_y+1) 
    grid2 = [[' '] * (max_x+1) for _ in range(max_y+1)]
    
    #print(grid==grid2)
    
    for x, y in points:
        grid[int(y)][int(x)] = '#'
        grid2[int(y)][int(x)] = '#'
        
    # for row in grid:
    #     print(''.join(row))
        
    # for row in grid2:
    #     print(''.join(row))
            

        
    results = '\n'.join(''.join(row) for row in grid2)
        
    
    return '\n'+results

@time_wrap
def day():
    
    data = read_input(_DAY, test=False)
    points, folds = split_data(data)

    p1, final_points = part_1(points, folds)
    p2 = part_2(final_points)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()
