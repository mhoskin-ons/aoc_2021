from aoc.read import read_input
from aoc.utilities import time_wrap

from itertools import groupby


_DAY = 2


def part_1(data):
    """
    Completes part 1 of day 2, sorts data, groups by command and sums,
    then returns the result

    Parameters
    ----------
    data : list[list]
        Raw data, of form ['command' 'value'].

    Returns
    -------
    answer : int
        forward value * total depth where total depth is down - up

    """
    results = {}
    sort_data = data.copy()
    sort_data.sort()
    
    for key,values in groupby(data, lambda t: (t[0])):#, t[1])):
    
        results[key] = sum(int(v[1]) for v in values)
    
    answer = results['forward'] * (results['down'] - results['up'])

    return(answer)


def part_2(data):
    """
    Completes part 2 of day 2, doesn't sort, just loops through the data,
    adjusts aim, lateral position, and vertical position accordingly

    Parameters
    ----------
    data : list[list]
        Raw data, of form ['command' 'value'].

    Returns
    -------
    answer : int
        forward value * total depth where total depth is down - up

    """

    unsorted_data = data.copy()
    
    aim = 0
    lat = 0
    vert = 0
    
    for order, value in unsorted_data:
        
        if order == 'down':
            aim += int(value)
        elif order == 'up':
            aim -= int(value)
        elif order == 'forward':
            lat += int(value)
            vert += int(value) * aim
            
    answer = lat * vert

    return(answer)
        

#a is unused, but essential to make autoreloading work from main script
@time_wrap
def day(a=1):
    
    data = read_input(_DAY, split=" ", sort=False, test=False)

    p1 = part_1(data)
    p2 = part_2(data)
    
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    


if __name__ == "__main__":
    
    p1, p2 = day()