#Matt Layman CS213 solver.py
import rubik

from collections import deque                             #deque imported for list manipulation

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start to end position.
    Returns a list of moves and assumes the rubik.quarter_twists move set.
    """

    if start == end: return []                             #if no shortest path exists (start==end), return empty list
    
    fparents = {start: None}                               #first half parents
    sparents = {end: None}                                 #second half parents
    fmoves = {}                                            #first half moves
    smoves = {}                                            #second half moves
    for turn in rubik.quarter_twists:
        fmoves[turn] = turn                                #insert forward moves from quarter_twists
        smoves[rubik.perm_inverse(turn)] = turn            #insert reverse moves (starting from second half)
    forward = (fmoves, fparents, sparents)                 #set of moves and first/second half parents
    backward = (smoves, sparents, fparents)                #set of inverse moves with first/second half parents
    Q = deque([(start, forward), (end, backward), None])   #create new deque(quicklist) Q = (first half, second half, None)
    
    for x in range(7):                                     #for each move in quarter_twist
        while True:                                        #loop
            v = Q.popleft()                                #return leftmost element from Q
            if v is None:                                  #if at the end of Q (None)
                Q.append(None)                             #add None to Q
                break                                      #break from loop
            position = v[0]                                #set vertex to start or end
            moves, parents, otherparents = v[1]            #set moves, parents, other parents to forward or backward
            for i in moves:                                #start two way BFS
                nextpos = rubik.perm_apply(i, position)    #set node to search
                if nextpos in parents: continue            #if node in parents, continue
                parents[nextpos] = (moves[i], position)    #set parent pointer to node, vertex
                Q.append((nextpos, v[1]))                  #add expanded search to Q
                if nextpos in otherparents:                #if node discovered in both searches
                    fpath = path(nextpos, fparents)        #forward path set with node + parent pointers
                    spath = path(nextpos, sparents)        #backward path set with node + parent pointers
                    spath.reverse()                        #must reverse the inverse path before joining it with forward path
                    return fpath + spath                   #return list of moves for the shortest path (forward + backward moves)
    
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
