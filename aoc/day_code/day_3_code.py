from aoc.read import read_input
from aoc.utilities import time_wrap


_DAY = 3


@time_wrap
def day():
    
    data = read_input(_DAY,test=True)
    
    p1 = 1
    p2 = 2
    
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    

if __name__ == "__main__":
    
    p1, p2 = day()