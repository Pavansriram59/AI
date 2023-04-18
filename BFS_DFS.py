class Graph:
    def printGraph(self,graph):
        for k,v in graph.items():
            print(f'{k} -> {v}')

    def bfs(self,graph,node):
        visited = [] # List for visited nodes.
        queue = []     #Initialize a queue

        visited.append(node)
        queue.append(node)

        while queue:          # Creating loop to visit each node
            m = queue.pop(0) 
            print (m, end = " ") 

            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    
    def dfs(self,graph,node):
        visited=set()
        if node not in visited:
            print (node,end=" ")
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(graph, neighbour)
 
 

# edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)]
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

graph = Graph()
graph.printGraph(edges)
print("Implementing BFS:")
graph.bfs(edges,0)
print("\nImplementing DFS:")
graph.dfs(edges,0)