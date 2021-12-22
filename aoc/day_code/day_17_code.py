from aoc.read import read_input
from aoc.utilities import time_wrap

import math

_DAY = 17


def part_1(y_min, y_0=0):
    """ Returns solution for part 1 
    Assumes that the target area is below and to the right
    - Y position works like the following: 10, 9, 8, ... -7, -8, -9 etc
    - The highest y peak comes with the highest initial y velocity
    - The highest y velocity on the descent just scrapes the bottom of the target
    - When the probe reaches y = 0 on the descent, its velocity is -(Vy0 + 1)
    - So the min value of y can show us the max velocity, and thus the max height
    """
    
    vy_max = abs(y_0 - y_min) - 1
    
    max_height = 0.5 * vy_max * (vy_max + 1)
    
    return max_height
    
    
def part_2(x_tar_min, x_tar_max,
           y_tar_min, y_tar_max,
           x_0=0, y_0=0):
    """ Returns solution for part 2 
    Again assumes target is below and to the right
    -min vx only just reaches the left edge
    -max vx is right edge in one shot
    -min vy is -max_vy - straight down
    -max vy found in part 1
    
    """
    
    vx_min = math.floor(0.5 + math.sqrt(2*x_tar_min - 0.25))
    vx_max = x_tar_max
    vy_min = -abs(y_0 - y_tar_min)
    vy_max = abs(y_0 - y_tar_min) - 1
    
    
    for vy in range(vy_min, vy_max + 1):
        y = 0
        steps = []
        step = 0
        while y_tar_min < y:
            step += 1
            y += vy
            vy -= 1
            
            if y >= y_tar_min & y <= y_tar_max:
                steps.append(step)
            
        print(vy, steps)
    
    
    return 2

@time_wrap
def day():
    
    data = read_input(_DAY, test=False)[0]
    split = data.split('=')
    x_tar_min = int(split[1].split('..')[0])
    x_tar_max = int(split[1].split('..')[1].split(',')[0])
    y_tar_min = int(split[2].split('..')[0])
    y_tar_max = int(split[2].split('..')[1])

    p1 = part_1(y_tar_min)
    p2 = part_2(x_tar_min, x_tar_max,
                y_tar_min, y_tar_max)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()
