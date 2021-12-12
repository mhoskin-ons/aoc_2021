from aoc.read import read_input
from aoc.utilities import time_wrap


_DAY = 10

_OPENERS = "([{<"
_CLOSERS = ")]}>"

_CHUNKS = {c:o for o, c in zip(_OPENERS, _CLOSERS)}
_CHUNKS_OC = {o:c for o, c in zip(_OPENERS, _CLOSERS)}


def parts(data):
    """ Returns solution for both parts """
    
    illegals = {closer:0 for closer in _CLOSERS}
    p2_scores = []
    
    for line in data:
        open_chunks = {opener:0 for opener in _OPENERS}
        
        recent_opens = [] 
        for char in line:

            #build a list of opening chars
            if char in _OPENERS:
                recent_opens.append(char)
                open_chunks[char] += 1
            
            #remove from the openers if chunk closed, or flag illegal
            elif char in _CLOSERS:
                if recent_opens[-1] == _CHUNKS[char]:
                    recent_opens.pop(-1)
                else: 
                    illegals[char] += 1
                    recent_opens = []
                    break #out of the for char in line loop
        
        #handle incomplete chunks
        if len(recent_opens) > 0: 
            completions = []
            #build reverse list of unfinished chunks
            while len(recent_opens) > 0:
                last = recent_opens.pop(-1)
                completions.append(_CHUNKS_OC[last])
        
            complete_score = 0
        
            for char in completions:
                complete_score *= 5
                complete_score += _CLOSERS.index(char) + 1
                
            p2_scores.append(complete_score)
        
     
    #p1 score            
    score = 3 * illegals[')'] + \
            57 * illegals[']'] + \
            1197 * illegals['}'] + \
            25137 * illegals['>']
            
    p2_scores.sort()           
    p2_score = p2_scores[len(p2_scores)//2]
            
    return score, p2_score
    
def part_1(data):
    """Returns solution for part 1"""
   
    p1, p2 = parts(data)
    
    return p1
 
def part_2(data):
    """ Returns solution for part 2 """
    
    p1, p2 = parts(data)
    
    return p2
    

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
