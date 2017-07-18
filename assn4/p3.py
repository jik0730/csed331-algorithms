import sys
import heapq


"""
Description: Main function
"""
def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        # Take inputs representing information to use
        inputs = sys.stdin.readline().split()
        numV, numE = map(int, inputs)

        # Make a undirected graph
        graph = makeGraph(numV, numE)

        # Shortest cycle
        shortestCycle = modifiedDijkstra(graph)
        print shortestCycle

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
        if graph[v2] == None:
            graph[v2] = [[v1,w]]
        else:
            graph[v2].append([v1,w])
        numE -= 1
    return graph


"""
Description: Implement Dijkstra algorithm
Input: A graph
Output: A shortest distance
"""
def modifiedDijkstra(g):
    path = [None]*len(g)
    prev = [None]*len(g)
    for i in range(len(path)):
        path[i] = [float('inf')]*len(g)
        prev[i] = [-1]*len(g)

    for s in range(len(path)):
        path[s][s] = 0
        heap = []
        for i in range(len(path[s])):
            heapq.heappush(heap, [path[s][i], i])
        while len(heap) != 0:
            u = heapq.heappop(heap)
            if g[u[1]] == None:
                continue
            for e in g[u[1]]:
                if (path[s][e[0]] > path[s][u[1]] + e[1] or path[s][s] == 0) and prev[s][u[1]] != e[0]:
                    path[s][e[0]] = path[s][u[1]] + e[1]
                    prev[s][e[0]] = u[1]
                    heapq.heappush(heap, [path[s][e[0]], e[0]])
        # print path[s]

    minCycle = float('inf')

    for i in range(len(path)):
        if path[i][i] < minCycle and path[i][i] != 0:
            minCycle = path[i][i]

    if minCycle == float('inf'):
        return -1
    else:
        return minCycle


if __name__ == "__main__":
    main()

