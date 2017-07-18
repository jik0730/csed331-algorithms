import sys


def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        n, m, L = map(int, sys.stdin.readline().split())
        graph = makeGraph(n, m)
        checkSol(graph, L)
        numOfTests -= 1


"""
Description: Make adjacency matrix graph representation
"""
def makeGraph(numV, numE):
    graph = [-1]*numV
    for i in range(numV):
        graph[i] = [-1]*numV
    while numE:
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u][v] = c
        graph[v][u] = c
        numE -= 1
    return graph

# If there does not exist connecting edge between consecutive nodes?
def checkSol(graph, L):
    route = map(int, sys.stdin.readline().split())
    distance = 0
    for i in range(0,len(route)-1):
        if graph[route[i]][route[i+1]] == -1:
            print 'No'
            return
        distance += graph[route[i]][route[i+1]]
    if graph[route[i+1]][route[0]] == -1:
        print 'No'
        return
    distance += graph[route[i+1]][route[0]]
    if distance <= L:
        print 'Yes'
    else:
        print 'No'


if __name__ == '__main__':
    main()