from aoc.read import read_input
from aoc.utilities import time_wrap

import numpy as np

_DAY = 7

def part_1(data):
    """ Returns solution for part 1 """
    
    #median value is the pivot point
    pivot = int(np.median(data))

    diff = sum([abs(d - pivot) for d in data])    
    
    return diff


def sum_to_n(n):
    """ n(n+1)/2 """
    
    return 0.5 * n * (n+1)

def part_2(data):
    """ Returns solution for part 2 """
    
    #mean is the pivot point, but need either floor or ceil depending on test
    #data versus the actual data, so do it for both, and return the minimum
    pivots = [np.floor(np.mean(data)), np.ceil(np.mean(data))]
        
    diffs = []
    for pivot in pivots:
        diff = int(sum([sum_to_n(abs(d - pivot)) for d in data]))
        diffs.append(diff)
    
    return min(diffs)

@time_wrap
def day():
    
    data = read_input(_DAY, split=',', test=False)[0]
    data = [int(d) for d in data]

    p1 = part_1(data)
    p2 = part_2(data)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()