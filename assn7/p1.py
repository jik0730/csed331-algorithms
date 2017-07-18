import sys
from collections import deque

"""
Description: Main function
"""
def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        n, m = map(int, sys.stdin.readline().split())

        # Make a graph, might need to be modified \
        # to implement LP in maximum flow
        graph = makeGraph(n, m)

        # Fold-Fulkerson algorithm to get max-flow
        max_flow = ff(graph, 0)
        print(max_flow)
        
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
            graph[v1] = {(v2, True): [w,0]} # To-vertex, capacity, flow, direction
        else:
            graph[v1][(v2, True)] = [w,0]
        if graph[v2] == None:
            graph[v2] = {(v1, False): [w,0]}
        else:
            graph[v2][(v1, False)] = [w,0]
        numE -= 1
    return graph


"""
Description: Fold-Fulkerson algorithm to get max-flow
Input: Undirected marked(actual direction from to) graph
"""
def ff(ugraph, max_flow):
    while True:
        flow = findAugmentedPath(ugraph)
        if flow == 0:
            return max_flow
        else:
            max_flow += flow



# Find augmented path using bfs
def findAugmentedPath(ugraph):
    # BFS
    # Set initial distances from node to destination
    numV = len(ugraph)
    distances = [float('inf')]*len(ugraph)

    # Initial condition in Breadth-first search
    q = deque()
    distances[0] = 0
    q.append(0)

    # Book keeping 
    bk = [None]*len(ugraph)

    # Iteration until finding shortest path to destination
    ####### Apply ff algorithm to find a-path
    ####### Apply ff algorithm to find a-path
    ####### Apply ff algorithm to find a-path
    found = False
    while len(q) != 0:
        u = q.popleft()

        if ugraph[u] == None:
            continue
            
        for v, d in ugraph[u]:
            c, f = ugraph[u][(v, d)]
            if (d and f==c) or (not d and f==0):
                continue
            if distances[v] == float('inf'):
                if d:
                    bk[v] = (u,c-f,d)
                else:
                    bk[v] = (u,f,d)
                q.append(v)
                distances[v] = distances[u] + 1
                if v == numV - 1:
                    found = True
                    break
        if found:
            break

    if not found:
        return 0
    else:
        flow = float('inf')
        while True:
            temp, toCompare, d = bk[v]
            v = temp
            if flow > toCompare:
                flow = toCompare
            if temp == 0:
                break
        # Flow update
        v = numV-1
        while True:
            temp, toCompare, d = bk[v]
            if d:
                ugraph[temp][(v,d)][1] += flow
                ugraph[v][(temp,not d)][1] += flow
            else:
                ugraph[temp][(v,d)][1] -= flow
                ugraph[v][(temp,not d)][1] -= flow
            v = temp
            if temp == 0:
                break
        return flow


if __name__ == '__main__':
    main()