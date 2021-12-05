from aoc.read import read_input
from aoc.utilities import time_wrap

from dataclasses import dataclass 

_DAY = 5
   

@dataclass
class Coord:
    x: int
    y: int
    
    # def __lt__(self, Coord):
        
    #     return ((self.x < Coord.x) & ()


def part_1(data):
    
    return data


def part_2(data):

    return data


def get_data(test=True):
    
    data = read_input(_DAY, test=True)
    
    all_points = []
    for d in data:
        points = d.split(' -> ')
        init_point = [int(p) for p in points[0].split(',')]
        final_point = [int(p) for p in points[1].split(',')]

        all_points.append((init_point, final_point))

    return all_points

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