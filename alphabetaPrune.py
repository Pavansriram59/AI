from math import *
MAX, MIN = 1000000, -1000000

def minimax(depth, nodeIndex, maximizingPlayer,values, alpha, beta,treeDepth):
  
    # Terminating condition. i.e
    # leaf node is reached
    if depth == treeDepth:
        return values[nodeIndex]
 
    if maximizingPlayer:
      
        best = MIN
 
        # Recur for left and right children
        for i in range(0, 2):
             
            val = minimax(depth + 1, nodeIndex * 2 + i,False, values, alpha, beta,treeDepth)
            best = max(best, val)
            alpha = max(alpha, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
      
    else:
        best = MAX
        # Recur for left and
        # right children
        for i in range(0, 2):
          
            val = minimax(depth + 1, nodeIndex * 2 + i,True, values, alpha, beta,treeDepth)
            best = min(best, val)
            beta = min(beta, best)
 
            # Alpha Beta Pruning
            if beta <= alpha:
                break
          
        return best
    
nodes = [5, 7, 12, 6, 3, 18, -9, 4]
treeDepth = log(len(nodes), 2)
print("The value is :", minimax(0, 0, True, nodes, MIN, MAX,treeDepth))