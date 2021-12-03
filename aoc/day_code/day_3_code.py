from aoc.read import read_input
from aoc.utilities import time_wrap


_DAY = 3


def part_1(data):
    
    bit_length = len(data[0])
    diag_length = len(data)
    
    sums = [0] * bit_length

    for diag in data:
        
        for bit in range(bit_length):
            sums[bit] += int(diag[bit])

    gamma = [0] * bit_length
    epsilon = gamma.copy()
    
    for bit in range(bit_length):
        gamma[bit] = str(int(sums[bit] > diag_length/2))
        epsilon[bit] = str(1 - int(gamma[bit]))

    pwr = int(''.join(gamma), 2) * int(''.join(epsilon), 2)
    
    return pwr

@time_wrap
def day():
    
    data = read_input(_DAY, split='', test=False)
    
    p1 = part_1(data)
    p2 = 2
    
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    

if __name__ == "__main__":
    
    p1, p2 = day()