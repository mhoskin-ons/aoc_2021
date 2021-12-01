from read import read_input



def compare_window(prev_wdw, data, idx, wdw_count):
    """
    

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
    
    curr_wdw = data[idx] + data[idx-1] + data[idx-2]
        
        
    if curr_wdw > prev_wdw:
        wdw_count += 1
        
    prev_wdw = curr_wdw
    
    return prev_wdw, wdw_count



data = read_input(1, cast_type=int, test=False)

inc_count = 0
wdw_count = 0
for idx in range(1,len(data)):
    if data[idx] > data[idx-1]:
        # print(data[idx], '>', data[idx-1])
        inc_count += 1
        
    if idx == 2:
        prev_wdw = data[idx-1] + data[idx-2] + data[idx-3]
        
        prev_wdw, wdw_count = compare_window(prev_wdw, data, idx, wdw_count)
                
    elif idx > 2:
        prev_wdw, wdw_count = compare_window(prev_wdw, data, idx, wdw_count)


        
        
print(inc_count)
print(wdw_count)