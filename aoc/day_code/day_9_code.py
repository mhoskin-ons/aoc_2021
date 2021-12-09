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
        

def part_1(data):
    """ Returns solution for part 2 """
    
    mins = []
    for row_idx, row in enumerate(data):
        for col in range(len(row)):
            
            if local_min(data, row_idx, col):
                mins.append(data[row_idx][col])
    
    


    mins = [int(v) for v in mins]
    risk_levels = sum(mins) + len(mins)
    
    return risk_levels
    
def part_2(data):
    """ Returns solution for part 2 """
    
    return 2


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