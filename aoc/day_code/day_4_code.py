from aoc.read import read_input
from aoc.utilities import time_wrap

from collections import Counter

_DAY = 4


def get_data(test=False):
    """
    Takes original read data, returns the first row split by commas,
    and the rest split into 5 line bingo grids

    Parameters
    ----------
    test : Bool, optional
        Test data or not. The default is False.

    Returns
    -------
    order : list[str]
        Bingo calls in order to match.
    tables : list[list[list[str]]]
        List of bingo tables to play with.
    """
    
    data = read_input(_DAY, split='', test=test)
    
    order = data[0].split(',')
    
    data = [d.split() for d in data]
    tables = []
    
    for init_row in range(2, len(data), 6):
        bingo_table = data[init_row : init_row+5]
        tables.append(bingo_table)
        
    
    return order, tables
    
   
def bingoed(table):
    """
    Checks whether a single table has bingoed - a full row or column of empty
    values.

    Parameters
    ----------
    table : list[list[str]]
        bingo table to validate .

    Returns
    -------
    bingoed : bool
        True if table has bingoed, False otherwise.

    """
    
    bingoed = False
    for row in table:
        if Counter(row)[''] == len(row):            
            bingoed = True
            
    # list(zip(*table)) transposes the list of lists
    for col in list(zip(*table)):
         if Counter(col)[''] == len(col):            
            bingoed = True       
    
    return bingoed

def parts(order, tables):
    """
    Completes both parts of day 4. Plays bingo game, and returns both first 
    winning and last winning scores. 

    Parameters
    ----------
    order : list[str]
        Bingo calls in order to match.
    tables : list[list[list[str]]]
        List of bingo tables to play with.

    Returns
    -------
    scores[0]
        Numeric score for part 1.
    scores[1]
        Numeric score for part 2.

    """
        
    scores = []

    #break out if no tables left uncompleted
    while len(tables) > 0:
        
        #loop through the bingo calls
        for call in order:
            bingoed_idxs = []
            
            #loop through the tables for each call, mark any matches as empty
            #strings, check if bingoed.
            #If bingoed, add index to list to remove, and add to list of scores
            #before removing matching indexes
            for table_idx, table in enumerate(tables):
                for row in table:
                    if call in row:
                        row[row.index(call)] = ''
    
                if bingoed(table):
                    bingoed_idxs.append(table_idx)
  
                    remaining_sum = sum([int(value) for row in table 
                                         for value in row if value != ''])
                    
                    scores.append(remaining_sum * int(call))

            #deal with complete tables to remove, flip indexes into reverse to 
            #avoid index shifts
            if len(bingoed_idxs) > 0:
                bingoed_idxs.sort(reverse=True)
                
                for removal_idx in bingoed_idxs:
                    tables.pop(removal_idx)
                
    return scores[0], scores[-1]
    

def part_1(order, tables):
    """Wrapper for just day 4 part 1 value"""
    
    return parts(order, tables)[0]


def part_2(order, tables):
    """Wrapper for just day 4 part 2 value"""

    return parts(order, tables)[1]


@time_wrap
def day():
    
    order, tables = get_data(test=False)
    
    p1, p2 = parts(order, tables)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, p2
    

if __name__ == "__main__":
    
    p1, p2 = day()