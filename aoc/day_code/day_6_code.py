from aoc.read import read_input
from aoc.utilities import time_wrap

from collections import Counter


_DAY = 6


def parts(data, days=80):
    """
    Generates number of fish for a specific day.
    
    Loops through days using an initial Counter of the data. Decreases ages of 
    fish by 1, births new fish where age is now -1, and rolls -1 age up to 6

    Parameters
    ----------
    data : list[int]
        Original numbers and ages of fish.
    days : int, optional
        Number of days to calculate for. The default is 80.

    Returns
    -------
    int
        total number of fish after specified day.

    """

    
    original_counts = dict(Counter(data))

    for day in range(1, days+1):
        counts = {k-1: v for k,v in original_counts.items()}
        
        if -1 in counts.keys():
            #fish birth
            counts[8] = counts[-1]
            
            #age rollover
            if 6 in counts.keys():
                counts[6] += counts[-1]
            else: 
                counts[6] = counts[-1]
            del counts[-1]
            
        original_counts = counts
            
    return sum(original_counts.values())

def part_1(data):
    """ Returns solution for part 1 """
    return parts(data, 80)

def part_2(data):
    """ Returns solution for part 2 """
    return parts(data, 256)


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