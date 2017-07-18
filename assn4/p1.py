import sys
from collections import deque


"""
Description: Main function
"""
def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        # Take inputs representing information to use
        inputs = sys.stdin.readline().split()
        numV, numE = map(int, inputs)

        # Make a graph representation which would be adjacency list
        graph = makeGraph(numV, numE)
        inGraph = makeInGraph(graph)

        # Do topological sorting
        stack = dfs(graph)
        stack.reverse()

        # Dynamic programming
        dist = [-1]*len(graph)
        dist[0] = 0
        for i in range(1,len(stack)):
            if inGraph[stack[i]] != None:
                dist[stack[i]] = max([dist[edge[0]]+edge[1] for edge in inGraph[stack[i]]])

        print dist[numV-1]
        numOfTests -= 1


"""
Description: To make a graph representation
Input: Number of vertices(int), edges(int)
Output: An adjacency list of the graph(list of list)
"""
def makeGraph(numV, numE):
    graph = [None]*numV
    while numE:
        inputs = sys.stdin.readline().split()
        v1, v2, w = map(int, inputs)
        if graph[v1] == None:
            graph[v1] = [[v2,w]]
        else:
            graph[v1].append([v2,w])
        numE -= 1
    return graph


"""
Description: To make a inGraph representation
Input: A graph
Output: An adjacency list of the graph(list of list)
"""
def makeInGraph(graph):
    inGraph = [None]*len(graph)
    for i in range(len(graph)):
        if graph[i] == None:
            continue
        for edge in graph[i]:
            if inGraph[edge[0]] == None:
                inGraph[edge[0]] = [[i,edge[1]]]
            else:
                inGraph[edge[0]].append([i,edge[1]])
    return inGraph


"""
Description: DFS using recursion and its supportive method
"""
def dfs(g):
    stack = []
    visited = [False]*len(g)
    for v in range(len(visited)):
        if not visited[v]:
            explore(g, v, visited, stack)
    return stack

def explore(g, v, visited, stack):
    visited[v] = True
    if g[v] == None:
        g[v] = []
    for e in g[v]:
        if not visited[e[0]]:
            explore(g, e[0], visited, stack)
    stack.append(v)


if __name__ == "__main__":
    main()