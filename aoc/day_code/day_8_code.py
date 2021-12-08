from aoc.read import read_input
from aoc.utilities import time_wrap

_DAY = 8

def part_1(data):
    """ Returns solution for part 1 """
    
    count = 0
    for entry in data:
        signal = entry[:10]
        output_value = entry[-4:]
        
        for val in output_value:
            if len(val) in [2,3,4,7]:
                count += 1
    
    return count

def contains(sub, sup):
    
    inc = [s for s in sup if s in sub]
    
    return len(inc) == len(sub)

def part_2(data):
    """ Returns solution for part 2 """
    
    sum = 0
    
    for entry in data:
        keys = {}
        signal = entry[:10]
        output_value = entry[-4:]
        
        keys[1] = [s for s in signal if len(s) == 2][0]
        keys[4] = [s for s in signal if len(s) == 4][0]
        keys[7] = [s for s in signal if len(s) == 3][0]
        keys[8] = [s for s in signal if len(s) == 7][0]
        
        digits_6 = [s for s in signal if len(s) == 6]
        keys[9] = [s for s in digits_6 if (contains(keys[4], s))][0]
        keys[0] = [s for s in digits_6 if (not contains(keys[4], s))][0]
        keys[6] = [s for s in digits_6 if (s not in keys[0] and s not in keys[9])][0]
        
        digits_5 = [s for s in signal if len(s) == 5]
        keys[3] = [s for s in digits_5 if (contains(keys[1], s))][0]
        keys[5] = [s for s in digits_5 if (contains(s, keys[6]))][0]
        keys[6] = [s for s in digits_5 if (s not in keys[3] and s not in keys[5])][0]
    
    return 2

@time_wrap
def day():
    
    data = read_input(_DAY, split=' ', test=False)

    p1 = part_1(data)
    p2 = part_2(data)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()