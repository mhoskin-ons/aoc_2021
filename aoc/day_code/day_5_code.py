from aoc.read import read_input
from aoc.utilities import time_wrap

from collections import Counter


_DAY = 5
   

def get_data(test=True):
    """
    Reads initial data, splits by arrow, gets coord values as list of tuple of
    list of ints

    Parameters
    ----------
    test : Bool, optional
        Whether to use test data or not. The default is True.

    Returns
    -------
    all_points : list[tuple[list[int]]]
        data for use in rest of exercises.

    """
    
    data = read_input(_DAY, test=test)
    
    all_points = []
    for d in data:
        points = d.split(' -> ')
        init_point = [int(p) for p in points[0].split(',')]
        final_point = [int(p) for p in points[1].split(',')]

        all_points.append((init_point, final_point))

    return all_points


def vertical(ends):
    """ Returns True if a vertical line between end points, else False """
    
    if ends[0][0] == ends[1][0]:
        vert = True
        
    else:
        vert = False

    return vert

def horizontal(ends):
    """ Returns True if a horizontal line between ends points, else False """
    
    if ends[0][1] == ends[1][1]:
        hozt = True
        
    else:
        hozt = False
        
    return hozt
            
def straight(ends):
    """ Returns True if either horizontal or vertical line, else False """
        
    if vertical(ends):
        # x1 = x2
        flat = True
    elif horizontal(ends):
        # y1 = y2
        flat = True
    else:
        flat = False
        
    return flat


def get_line_points(ends, diag=False):
    """
    Gets all points between end points of a line. Vert/Hozt by default, can 
    set diagonals if desired

    Parameters
    ----------
    ends : tuple[list[int]]
        start and end points of line.
    diag : Bool, optional
        Include diagonal lines. The default is False.

    Returns
    -------
    vals : list[tuple[int]]
        All points on the line.
        
    TODO:
        Could be much tidier, list comprehension put in helper function

    """
    
    vals = []
    if horizontal(ends):
        
        y = ends[0][1]
        x_lims = min(ends[0][0], ends[1][0]),\
                 max(ends[0][0], ends[1][0])
        
        for x in range(x_lims[0], x_lims[1]+1):
            
            vals.append((x, y))
                  
    elif vertical(ends):
        x = ends[0][0]
        y_lims = min(ends[0][1], ends[1][1]),\
                 max(ends[0][1], ends[1][1])
        
        for y in range(y_lims[0], y_lims[1]+1):
            vals.append((x,y))
            
    elif diag:
        #used only in part 2 if care about diagonal lines
        
        x_lims = ends[0][0], ends[1][0]
        x_asc = x_lims[0] < x_lims[1]
        
        if x_asc:
            x_vals = [x for x in range(x_lims[0], x_lims[1]+1)]
            
        else:
            x_vals = [x for x in range(x_lims[0], x_lims[1]-1, -1)]
            
        
        y_lims = ends[0][1], ends[1][1]
        y_asc = y_lims[0] < y_lims[1]
        
        if y_asc:
            y_vals = [y for y in range(y_lims[0], y_lims[1]+1)]
            
        else:
            y_vals = [y for y in range(y_lims[0], y_lims[1]-1, -1)]
        
    
        vals += zip(x_vals, y_vals)
            
    return vals


def part_1(all_points):
    """ Returns solution for part 1 """
    
    all_interim_points = []
    crossovers = set()
    for ends in all_points:
        if straight(ends):
            line_points = get_line_points(ends) #current line
            
            crossovers |= set(line_points) & set(all_interim_points)
            
            all_interim_points += line_points
            
            
    p1 = len(crossovers)
    
    return p1


def part_2(all_points):
    """ Returns solution for part 2 """
    
    all_interim_points = []
    crossovers = set()
    for ends in all_points:
        line_points = get_line_points(ends, diag=True) #current line
        
        crossovers |= set(line_points) & set(all_interim_points)
        
        all_interim_points += line_points
        

    p2 = len(crossovers)
    
    return p2

@time_wrap
def day():
    
    # data = read_input(_DAY, test=True)
    all_points = get_data(test=False)
    
    p1 = part_1(all_points)
    p2 = part_2(all_points)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    

if __name__ == "__main__":
    
    p1, p2 = day()