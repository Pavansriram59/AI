import copy
# graph = {}
# n = int(input("Enter the number of nodes : "))
# alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# for i in range(n):
#     c = int(input(f"Enter number of children of {alpha[i]} : "))
#     graph[alpha[i]] = []
#     for j in range(c):
#         name = input("Enter the child node name : ")
#         cost = int(input(f"Enter the cost to reach {name} from {alpha[i]} : "))
#         h = int(input(f"Enter the heuristic value of {name} : "))
#         graph[alpha[i]].append([cost,name,h])
def Astar(graph,start,goal):
    original = copy.deepcopy(graph)
    opened = [start]
    closed = []
    current_node = start
    path = start[1]
    while current_node[1] != goal:
        for child in graph[current_node[1]]:
            child[0] += current_node[0] + child[2] - current_node[2]
            opened.append(child)
        opened.sort()
        closed.append(current_node)
        opened.remove(current_node)
        current_node = opened[0]
        path += "-"+current_node[1]
    print(path)
    path = path.split('-')
    cost = 0 
    for i in range(0,len(path)-1):
        for g in original[path[i]]:
            if g[1] == path[i+1]:
                cost += g[0]
    print(cost)

G={'A': [[2, 'B', 4], [1, 'C', 2]],
 'B': [[5, 'D', 6]],
 'C': [[3, 'D', 6], [4, 'F', 0]],
 'D': [[2, 'F', 0]],
 'E': [[1, 'A', 3], [10, 'F', 0]],
 'F': []}
Astar(G,[0,'E',5],'F')