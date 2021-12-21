from aoc.read import read_input
from aoc.utilities import time_wrap

from copy import deepcopy

_DAY = 15


def neighbours(current, data):
    
    deltas = []
    valid_neighbours = []
    for i in range(-1, 2, 2):
        deltas.append((i, 0))
        deltas.append((0, i))
    
    
    for d in deltas:
        
        row = current[0] + d[0]
        col = current[1] + d[1]
        
        if row >= 0 and row < len(data):
            if col >= 0 and col < len(data[0]):
                valid_neighbours.append((row, col))
                
    return valid_neighbours

def part_1(data):
    """ Returns solution for part 1 """
    
    start = (0,0) #row, col
    goal = (len(data)-1, len(data[0])-1)
    
    frontier = [start]
    came_from = {}
    cost_to_point = {}
    came_from[start] = None
    cost_to_point[start] = 0#int(data[start[0]][start[1]])
    
    # test = 0
    
    while len(frontier) > 0:
        
        current = frontier.pop(0)
        # print(current)
        # if current == goal:
        #     break
        
        for neighbour in neighbours(current, data):
            
        
            neighbour_cost = data[neighbour[0]][neighbour[1]]
            # print(neighbour_cost)
            step_cost = int(neighbour_cost) + int(cost_to_point[current])
            # print(step_cost)    
            
            if neighbour in cost_to_point.keys():
                # print(neighbour)
                if step_cost < cost_to_point[neighbour]:
                    # print('cheaper')
                    cost_to_point[neighbour] = step_cost            
                    came_from[neighbour] = current
                    if neighbour not in frontier:
                        # print('add to frontier')
                        frontier.append(neighbour)

            else:
                # print('new')
                cost_to_point[neighbour] = step_cost
                came_from[neighbour] = current
                frontier.append(neighbour)
    
    # mapper = [[0,0,0,0,0,0,0] for _ in range(7)]
    # for row, col in cost_to_point.keys():
    #     mapper[row][col] = cost_to_point[(row, col)]
    
    # for i in mapper:
    #     print(i)
    
    
    lowest_risk = cost_to_point[goal]
    # print('test:{0}'.format(lowest_risk))
    
    
    # #### TEST ####
    
    s = 0
    goal = (len(data)-1, len(data[0])-1)
    s += int(data[goal[0]][goal[1]])
    
    while True:
        next_loc = came_from[goal]
        #print(next_loc)
        if next_loc == (0,0):
            break
        
        s+= int(data[next_loc[0]][next_loc[1]])
        goal = next_loc

    
    
    
    print(lowest_risk, s)
    
    return lowest_risk
    
def step_up(data, n):
    
    stepped_data = []
    
    for idx, row in enumerate(data):
        
        stepped_data.append(''.join([str(int(v) + n) if int(v) + n <= 9 else str(int(v) + n - 9)
                                     for v in row]))
        
    return stepped_data
        
def part_2(data):
    """ Returns solution for part 2 """
    
    #make new single column equal to additions from 0 to 9 inc
    long_data = deepcopy(data)
    for s in range(1,10):
        long_data.extend(step_up(data, s))
    
    #make 5 columns (hardcoded for now, could be expanded)
    cols = []
    for col in range(5):
        cols.append(long_data[col*len(data):(5+col)*len(data)])
        
    #combine columns staggered
    new_data = []
    for (c1, c2, c3, c4, c5) in zip(*cols):
        new_data.append(c1+c2+c3+c4+c5)
    

    return part_1(new_data)

@time_wrap
def day():
    
    data = read_input(_DAY, test=False)

    p1 = part_1(data)
    p2 = part_2(data)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()



# s = 0
# goal = (9,9)
# s += int(data[goal[0]][goal[1]])

# while True:
#     next_loc = came_from[goal]
#     if next_loc == (0,0):
#         break
#     s+= int(data[next_loc[0]][next_loc[1]])
#     goal = next_loc


