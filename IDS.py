class Graph:

    def __init__(self,graph) -> None:
        self.graph=graph

    def printGraph(self,graph):
        for k,v in graph.items():
            print(f'{k} -> {v}')

    # * Depth Limited Search
    def dls(self,src,target,maxDepth):
        if src==target:
            return True
        
        if maxDepth<=0:return False

        for i in self.graph[src]:
            if(self.dls(i,target,maxDepth-1)):
                return True
        return False

    # todo IDDFS to search if target is reachable from v.
    # todo It uses recursive DLS()
    def ids(self,src,target,maxDepth):
        for i in range(maxDepth):
            if (self.dls(src, target, i)):
                return True
        return False


edges={}
n=int(input("Enter the no of vertices:"))
for i in range(n):
    if i not in edges:
        edges[i]=[]
        e=int(input(f"Enter the no of edges for vertex {i} :"))
        for _ in range(e):
            x=int(input("Enter the vertex:"))
            edges[i].append(x)
        

print(edges)

graph = Graph(edges)
graph.printGraph(edges)
maxDepth=int(input("Enter the max. depth:"))
goal=int(input("Enter the goal node:"))

print("Implementing Iterative deeping:")

if graph.ids(0, goal, maxDepth):
    print ("Target is reachable from source within max depth")
else :
    print ("Target is NOT reachable from source within max depth")