from aoc.read import read_input
from aoc.utilities import time_wrap


_DAY = 5
   

def part_1(data):
    
    return data


def part_2(data):

    return data


@time_wrap
def day():
    
    data = read_input(_DAY, test=True)
    
    p1 = part_1(data)
    p2 = part_2(data)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    

if __name__ == "__main__":
    
    p1, p2 = day()