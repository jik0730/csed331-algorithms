import sys
import heapq
import time


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
        start_time = time.time()
        shortestCycle = modifiedDijkstra(graph)
        # print ('Calculate shortest cycle takes %s' %(time.time()-start_time))
        if shortestCycle == float('inf'):
            print (-1)
        else:
            print (shortestCycle)

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
    minCycle = float('inf')
    for u in range(len(g)):
        if g[u] == None:
            continue
        for edge in g[u]:
            v = edge[0]
            w = edge[1]
            # edge[1] = float('inf')
            g[u].remove(edge)
            shortest = dijkstra_2(g, u, v, minCycle)
            g[u].append(edge)
            # edge[1] = w
            if shortest != float('inf') and minCycle > shortest + w:
                minCycle = shortest + w
    return minCycle


"""
Description: Dijkstra
"""
def dijkstra(g, u, v1, minCycle):
    dist = [float('inf')]*len(g)
    prev = [-1]*len(g)
    dist[u] = 0
    heap = []
    for i in range(len(g)):
        heapq.heappush(heap, [dist[i], i])
    while len(heap) != 0:
        v = heapq.heappop(heap)
        if g[v[1]] == None:
            continue
        for e in g[v[1]]:
            if e[1] > minCycle:
                continue
            efrom = v[1]
            eto = e[0]
            if dist[eto] > dist[efrom] + e[1] and minCycle > dist[efrom] + e[1]:
                dist[eto] = dist[efrom] + e[1]
                prev[eto] = efrom
                heapq.heappush(heap, [dist[eto], eto])
    if dist[v1] == float('inf'):
        return float('inf')
    return dist[v1]


"""
Description: Dijkstra version 2
"""
def dijkstra_2(g, u, v1, minCycle):
    dist = [float('inf')]*len(g)
    
    distance = float('inf')
    visited = [False]*len(g)
    dist[u] = 0
    heap = []
    heapq.heappush(heap, [dist[u], u])
    while len(heap) != 0:
        v = heapq.heappop(heap)
        if g[v[1]] == None:
            continue
        if visited[v[1]] == True:
            continue
        else:
            visited[v[1]] = True
        if v[1] == v1:
            distance = v[0]
            break
        for e in g[v[1]]:
            heapq.heappush(heap, [e[1]+v[0], e[0]])
    # return dist[v1]
    return distance


if __name__ == "__main__":
    main()

