from aoc.read import read_input
from aoc.utilities import time_wrap


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
    
    while len(frontier) > 0:
        
        current = frontier.pop(0)
        
        if current == goal:
            break
        
        for neighbour in neighbours(current, data):
            
        
            neighbour_cost = data[neighbour[0]][neighbour[1]]
            step_cost = int(neighbour_cost) + int(cost_to_point[current])
                
            if neighbour in cost_to_point.keys():
                if step_cost < cost_to_point[neighbour]:
                    cost_to_point[neighbour] = step_cost            
                    came_from[neighbour] = current

            else:
                cost_to_point[neighbour] = step_cost
                came_from[neighbour] = current
                frontier.append(neighbour)
    
    
    lowest_risk = cost_to_point[goal]
    
    return lowest_risk
    
        
def part_2(data):
    """ Returns solution for part 2 """
    
    return 2

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
