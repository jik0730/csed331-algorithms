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

        # Derive shortest distance
        shortestDist = dijkstra(graph)
        print shortestDist

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
def dijkstra(g):
    dist = [float('inf')]*len(g)
    prev = [-1]*len(g)
    dist[0] = 0
    heap = []
    for i in range(len(g)):
        heapq.heappush(heap, [dist[i], i])
    while len(heap) != 0:
        v = heapq.heappop(heap)
        if g[v[1]] == None:
            continue
        for e in g[v[1]]:
            efrom = v[1]
            eto = e[0]
            if dist[eto] > dist[efrom] + e[1]:
                dist[eto] = dist[efrom] + e[1]
                prev[eto] = efrom
                heapq.heappush(heap, [dist[eto], eto])
    if dist[len(g)-1] == float('inf'):
        return -1
    return dist[len(g)-1]


if __name__ == "__main__":
    main()

    