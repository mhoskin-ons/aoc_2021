from aoc.read import read_input
from aoc.utilities import time_wrap


def compare_window(prev_wdw, data, idx, wdw_count, wdw_size=3):
    """
    Compares window against the previous, of size specified.
    Provides a count of number of windows that summed are larger than prev

    Parameters
    ----------
    prev_wdw : int
        previous summed window.
    data : list[int]
        full data set.
    idx : int
        top level working index for end of second window.
    wdw_count : int
        incrementing count for condition.

    Returns
    -------
    prev_wdw : int
        previous summed window.
    wdw_count : int
        incrementing count for condition.

    """
    
    curr_wdw = sum(data[idx-(wdw_size-1) :idx+1])
        
        
    if curr_wdw > prev_wdw:
        wdw_count += 1
        
    prev_wdw = curr_wdw
    
    return prev_wdw, wdw_count


@time_wrap
def day(wdw_size = 3):

    data = read_input(1, cast_type=int, test=False)
    
    inc_count = 0
    wdw_count = 0
    for idx in range(1,len(data)):
        #used for part 1
        if data[idx] > data[idx-1]:
            inc_count += 1
            
        #used for part 2
        if idx == wdw_size-1:
            prev_wdw = sum(data[idx-(wdw_size):idx])
            
            prev_wdw, wdw_count = compare_window(prev_wdw, data, idx, wdw_count)
                    
        elif idx > wdw_size-1:
            prev_wdw, wdw_count = compare_window(prev_wdw, data, idx, wdw_count)
    
    print("Day 1 Part 1: {0}".format(inc_count))
    print("Day 1 Part 2: {0}".format(wdw_count))

    return(inc_count, wdw_count)
        
        

if __name__ == "__main__":
    
    p1, p2 = day()