import sys
from collections import deque

numOfTests = int(sys.stdin.readline())

for i in range(numOfTests):
    inputs = sys.stdin.readline().split()
    numV, numE, k = map(int, inputs)
    
    # Make a graph representation which would be adjacency list
    graph = [None]*numV
    tGraph = [None]*numV
    sortedEdges = []
    for j in range(numE):
        inputs = sys.stdin.readline().split()
        e1, e2, p = map(int, inputs)
        sortedEdges.append(p)
        if graph[e1] == None:
            graph[e1] = [[e2,p]]
            tGraph[e1] = [[e2,p]]
        else:
            graph[e1].append([e2,p])
            tGraph[e1].append([e2,p])

    # Sorted edges
    sortedEdges.sort()

    # Looping until converge in binary search
    low = 0
    high = len(sortedEdges)-1
    while low <= high:
        pos = (low+high)/2
        # print "pos: ", pos
        # Choose one using binary search
        mid = sortedEdges[pos]

        # Make the graph with weights 0 or 1 (~ing) --> Need to be modified
        for m in range(len(graph)):
            if graph[m] == None:
                continue
            for n in range(len(graph[m])):
                if graph[m][n][1] > mid:
                    tGraph[m][n][1] = 1
                else:
                    tGraph[m][n][1] = 0

        # 0-1 BFS
        q = deque()
        distances = [float('inf')]*numV
        distances[0] = 0
        q.append([0,0])

        # Iteration until finding shortest path to destination
        solution = -1
        while len(q) != 0:
            # found = False
            # print q
            u = q.popleft()

            if u[0] == numV - 1:
                solution = distances[u[0]]
                break

            if tGraph[u[0]] == None:
                continue
                
            for v in tGraph[u[0]]:
                # if distances[v[0]] == float('inf'):
                if distances[v[0]] > distances[u[0]] + v[1]:
                    distances[v[0]] = distances[u[0]] + v[1]
                    if v[1] == 1:
                        q.append(v)
                    else:
                        q.appendleft(v)
            #         if v[0] == numV - 1:
            #             found = True
            #             solution = distances[v[0]]
            #             break
            # if found:
            #     break

        # print "mid: ", mid, "solution:", solution, "numE:", numE, "tGraph:", tGraph
        if solution >= 1:
            # go right in binary search
            low = pos+1
        elif solution == 0:
            # go left in binary search

            # Unit BFS
            q2 = deque()
            distances2 = [float('inf')]*numV
            distances2[0] = 0
            q2.append([0,0])

            # Iteration until finding shortest path and length
            solution2 = -1
            while len(q2) != 0:
                found2 = False
                u2 = q2.popleft()

                if tGraph[u2[0]] == None:
                    continue
                    
                for v2 in tGraph[u2[0]]:
                    if distances2[v2[0]] == float('inf'):
                        if v2[1] == 0:
                            q2.append(v2)
                            distances2[v2[0]] = distances2[u2[0]] + 1
                            if v2[0] == numV - 1:
                                found2 = True
                                solution2 = distances2[v2[0]]
                                break
                if found2:
                    break

            if solution2 == -1:
                print ("Something went wrong.")
            elif solution2 <= k:
                high = pos-1
            elif solution2 > k:
                low = pos+1
            # else:
            # print "WTF! solution2 is", solution2
            # print "And the value is", mid
        else:
            # if all pathes length are less than k
            # print "HI"
            break

    # print "solution is", solution, "solution2 is", solution2

    if solution >= 1:
        print (sortedEdges[pos+1]+1)
    elif solution == 0:
        if solution2 <= k:
            print (mid+1)
        elif pos >= len(sortedEdges) - 1:
            print ("-1")
        else:
            print (sortedEdges[pos+1]+1)
    else:
        print (solution)

