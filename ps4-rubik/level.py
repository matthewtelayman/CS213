#Matt Layman CS213 level.py
import rubik

from collections import deque                             #deque imported for list manipulation

def positions_at_level(level):
    """
    Using BFS, returns the number of cube configurations that are
    exactly a given number of levels away from the starting position
    (rubik.I), using the rubik.quarter_twists move set.
    """
    moves = {}                                             #set a list of moves
    for turn in rubik.quarter_twists:
        moves[turn] = turn                                 #insert moves from quarter_twist
    Q = deque([moves, None])                               #create new deque Q =(moves, None)
    
    for x in range(level):                                 #for each move in level
        while True:                                        #loop
            v = moves.popleft()                            #return leftmost element from Q
            if v is None:                                  #if at the end of Q (None)
                Q.append(None)                             #add None to Q
                break                                      #break from loop
            position = v[0]                                #set vertex to move
            otherparents = v[1]                            #set parent pointers
            for i in moves:                                #start BFS
                nextpos = rubik.perm_apply(i, position)    #set node to search
                parents[nextpos] = (moves[i], position)    #set parent pointer to node, vertex
                Q.append((nextpos, v[1]))                  #add expanded search to Q
                if nextpos in otherparents:                #if node discovered in both searches
                    path = path(nextpos, parents)          #path with parent pointers
                    return len(path)                       #return number of list of moves to solved state (rubiks.I)
    
    return None                                            #else return None
  
def path(pos, parents):                                    #returns path between node and parents (parent pointers)
    path = []                                              #path = empty list
    while True:                                            #loop
        movepos = parents[pos]                             #set move position to parent pointer
        if movepos is None:                                #if no parent pointers
          path.reverse()                                   #invert parent pointers (path to node)
          return path                                      #return path
        path.append(movepos[0])                            #add current parent pointer to list
        pos = movepos[1]                                   #move to next parent pointer
