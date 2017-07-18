import sys
import itertools


def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        n, m = map(int, sys.stdin.readline().split())
        graph = makeGraph(n, m)
        route_distance = TSP(graph)
        if route_distance == float('inf'):
            print -1
        else:
            print route_distance
        numOfTests -= 1


"""
Description: Make adjacency matrix graph representation
"""
def makeGraph(numV, numE):
    graph = [float('inf')]*numV
    for i in range(numV):
        graph[i] = [float('inf')]*numV
    while numE:
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u][v] = c
        graph[v][u] = c
        numE -= 1
    return graph


"""
Description: TSP algorithm by dynamic programming
"""
def TSP(graph):
    n = len(graph)
    C = {(frozenset([0]), 0): 0}
    for s in range(2, n+1):
        for S in [frozenset(subset) for subset in itertools.combinations(range(n), s)]:
            if 0 not in S:
                continue
            C[(S, 0)] = float('inf')
            for j in S - frozenset([0]):
                C[(S, j)] = min([C[S-frozenset([j]),i]+graph[i][j] for i in S-frozenset([j])])
    print C
    return min([C[frozenset(range(n)),j]+graph[j][0] for j in range(n)])

if __name__ == '__main__':
    main()