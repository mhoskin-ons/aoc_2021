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
    """ If sub is inside sup, return True """
    
    inc = [s for s in sup if s in sub]
    
    return len(inc) == len(sub)


def key_code(keys, n):
    """ Finds n in the values of dictionary keys, and returns the matching key """
    
    return list(keys.keys())[list(keys.values()).index(n)]

def part_2(data):
    """ Returns solution for part 2 """
    
    sum_all = 0
    
    for entry in data:
        keys = {}
        signal = entry[:10]
        output_value = entry[-4:]
        
        keys[''.join(sorted([s for s in signal if len(s) == 2][0]))] = 1
        keys[''.join(sorted([s for s in signal if len(s) == 4][0]))] = 4
        keys[''.join(sorted([s for s in signal if len(s) == 3][0]))] = 7
        keys[''.join(sorted([s for s in signal if len(s) == 7][0]))] = 8
        
        digits_6 = [s for s in signal if len(s) == 6]
        keys[''.join(sorted([s for s in digits_6 if (contains(key_code(keys, 4), s))][0]))] = 9
        keys[''.join(sorted([s for s in digits_6 if (not contains(key_code(keys, 4), s) and\
                                                     contains(key_code(keys, 1),s))][0]))] = 0
        keys[''.join(sorted([s for s in digits_6 if ''.join(sorted(s)) not in keys.keys()][0]))] = 6
        
        digits_5 = [s for s in signal if len(s) == 5]
        keys[''.join(sorted([s for s in digits_5 if (contains(key_code(keys, 1), s))][0]))] = 3
        keys[''.join(sorted([s for s in digits_5 if (contains(s, key_code(keys,6)))][0]))] = 5
        keys[''.join(sorted([s for s in digits_5 if ''.join(sorted(s)) not in keys.keys()][0]))] = 2
        
        
        n = []
        for ov in output_value:
            
            ov = ''.join(sorted(ov))
            
            n.append(str(keys[ov]))
            
        score = int(''.join(n))
        
        sum_all += score
            
    return sum_all

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