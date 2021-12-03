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



def most_common_bit(data, column, val='oxy'):
    
    diag_length = len(data)
    sums = 0
    
    for diag in data:
        sums += int(diag[column])
        
    
    if int(sums) == diag_length/2:
        if val=='oxy':
            mcb = '1'
        else:
            mcb = '0'
    else:
        mcb = str(int(sums > diag_length / 2))

        
        
    return mcb
    
def least_common_bit(data, column):
    
    return str(1 - int(most_common_bit(data, column)))


def part_2(data):
    
    oxy_data = data.copy()
    co2_data = data.copy()
    
    oxy_idx = 0
    while len(oxy_data) > 1:
        
        mcb = most_common_bit(oxy_data, oxy_idx)
        
        oxy_data = [o for o in oxy_data if o[oxy_idx] == mcb]
        
        oxy_idx += 1
        
        
    co2_idx = 0
    while len(co2_data) > 1:
        
        lcb = least_common_bit(co2_data, co2_idx)
        
        co2_data = [c for c in co2_data if c[co2_idx] == lcb]
        
        co2_idx += 1   
        
    lf_support = int(oxy_data[0], 2) * int(co2_data[0], 2)
    
    return lf_support



@time_wrap
def day():
    
    data = read_input(_DAY, split='', test=False)
    
    p1 = part_1(data)
    
    p2 = part_2(data)
    
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    

if __name__ == "__main__":
    
    p1, p2 = day()