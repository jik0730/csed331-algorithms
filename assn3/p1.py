import sys
from collections import deque

numOfTests = int(sys.stdin.readline())

for i in range(numOfTests):
    inputs = sys.stdin.readline().split()
    numV, numE = map(int, inputs)
    
    # Make a graph representation which would be adjacency matrix
    graph = [None]*numV
    for j in range(numE):
        inputs = sys.stdin.readline().split()
        e1, e2 = map(int, inputs)

        if graph[e1] == None:
            graph[e1] = [e2]
        else:
            graph[e1].append(e2)

    # Set initial distances from node to destination
    distances = [float('inf')]*numV

    # Initial condition in Breadth-first search
    q = deque()
    distances[0] = 0
    q.append(0)

    # Iteration until finding shortest path to destination
    solution = -1
    while len(q) != 0:
        found = False
        u = q.popleft()

        if graph[u] == None:
            continue
            
        for v in graph[u]:
            if distances[v] == float('inf'):
                q.append(v)
                distances[v] = distances[u] + 1
                if v == numV - 1:
                    found = True
                    solution = distances[v]
                    break
        if found:
            break

    print(solution)



