from aoc.read import read_input
from aoc.utilities import time_wrap

from collections import Counter

_DAY = 14


def split_data(data):
    """
    Turn messy data source with multiple values into two separate variables

    Parameters
    ----------
    data : list[str]
        initial raw data with both template and rule values

    Returns
    -------
    template : str
        initial string to use
    rules : dict{str:str}
        mapper of character pairs to character to insert

    """
      
    template = data[0]
    rules = data[2:]
    
    rules = [r.split(' -> ') for r in rules]
    rules = {r[0]:r[1] for r in rules}

    return template, rules


def part_1(template, rules, steps=10):
    """ Returns solution for part 1 
    Inefficient solution """
        
    for step in range(steps):
        
        split_template = [template[0]]
        
        for idx in range(0, len(template)-1):
            pair = template[idx] + template[idx+1]
            inserted = pair[0] + rules[pair] + pair[1]
            
            split_template.append(inserted[1:])
            

        template = ''.join(split_template)
        
    c = Counter(template)
    
    max_count = max(c.values())
    min_count = min(c.values())
    
    return max_count - min_count
    
    
def part_2(template, rules, steps=40):
    """ Returns solution for part 2 
    Efficient solution using the lanternfish method - deals with counts
    of pairs rather than generating all of the strings!"""
    
    #counts stores pairs of letters, create initial based on template
    counts = {}

    for idx in range(0, len(template)-1):
        pair = template[idx] + template[idx+1]
        if pair in counts.keys():
            counts[pair] += 1
        else:
            counts[pair] = 1
        
  
    #make triplets by inserting rule values, split up, and add to counter
    for step in range(steps):
        
        #counter for this step
        temp_counts = {}
        
        for pairs, instances in counts.items():
            triplet = pairs[0] + rules[pairs] + pairs[1]
            
            #tuple of new pairs
            new_pairs = triplet[:2], triplet[1:]

            #include or increment
            for np in new_pairs:
                if np in temp_counts.keys():
                    temp_counts[np] += instances
                else:
                    temp_counts[np] = instances
        
        counts = temp_counts
        
    #load letter counts with initial letter of template string
    #this allows us to add only the second character of all other pairs
    #to avoid duplication - the very first character at the beginning is
    #the very first character at the end, while every other character will 
    #appear on the right hand side of a pair. 
    letter_counts = {template[0]:1}
    for pair, value in counts.items():
        letter = pair[1]
        if letter in letter_counts.keys():
            letter_counts[letter] += value
        else:
            letter_counts[letter] = value
    
    max_count = max(letter_counts.values())
    min_count = min(letter_counts.values())
        
    return max_count - min_count

@time_wrap
def day():
    
    data = read_input(_DAY, test=False)
    
    template, rules = split_data(data)

    p1 = part_1(template, rules)
    p2 = part_2(template, rules)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()
