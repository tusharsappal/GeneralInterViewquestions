# Python program to print DFS traversal from a
# given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:
    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, v):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            s = queue.pop(0)
            print s,
            # Get all adjacent vertices of the dequeued
            # vertex s. If a adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print "Following is DFS from (starting from vertex 2)"
g.BFS(2)
