from binarytree import *
from math import *

# nodes=[0,3, 5, 2, 9, 12, 5, 23]
nodes =[0,1, 3, 8, 2, 11, 13]
binary_tree = build(nodes)
print(binary_tree)

def minimax (curDepth, nodeIndex,maxTurn, nodes,targetDepth): 
    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return nodes[nodeIndex]
     
    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,False, nodes, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,False, nodes, targetDepth))
     
    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,True, nodes, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1 ,True, nodes, targetDepth))
        
treeDepth1=binary_tree.height


# print(treeDepth1,treeDepth2)
print("The optimal value is:")
print(minimax(0,0,True,nodes,treeDepth1))