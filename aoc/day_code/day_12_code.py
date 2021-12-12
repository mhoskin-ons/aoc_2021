from aoc.read import read_input
from aoc.utilities import time_wrap


_DAY = 12

def build_graph(data):
    
    graph = {}
    for r in data:
        if r[0] in graph:
            graph[r[0]].append(r[1])
        else:
            graph[r[0]] = [r[1]]
            
        if r[1] in graph:
            graph[r[1]].append(r[0])
        else:
            graph[r[1]] = [r[0]]
            
    return graph

#def step(graph, path)

def part_1(graph):
    """ Returns solution for part 1 """
    
    paths = []
    
    node = 'start'
    path = ['start']
    for loc in graph[node]:
        if loc not in path:
            #add loc to path
        elif loc.isupper():
            #add loc to path
        if loc == 'end':
            
        current_path = path += [loc]
        
        
    
    return 1
    
    
def part_2(graph):
    """ Returns solution for part 2 """
    
    return 2

@time_wrap
def day():
    
    data = read_input(_DAY, test=True, split='-')
    graph = build_graph(data)

    p1 = part_1(graph)
    p2 = part_2(graph)
        
    print("Day {0} Part 1: {1}".format(_DAY, p1))
    print("Day {0} Part 2: {1}".format(_DAY, p2))
    
    return p1, 2
    
    
if __name__ == "__main__":
    
    p1, p2 = day()
