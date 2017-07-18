import sys


def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        s = int(sys.stdin.readline())
        seq = map(int, sys.stdin.readline().split())
        print(LNDS(seq, s))
        numOfTests -= 1


"""
Description: To make a graph representation
Input: Number of vertices(int)
Output: An adjacency list of the graph(list of list)
"""
def makeGraph(seq):
    n = len(seq)
    graph = [None]*n
    for v1 in range(n):
        for v2 in range(v1+1, n):
            if seq[v2] >= seq[v1]:
                if graph[v1] == None:
                    graph[v1] = [v2]
                else:
                    graph[v1].append(v2)
    return graph


"""
Description: Compute longest subsequence
"""
def longestDistance(seq):
    n = len(seq)
    L = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if seq[j] >= seq[i]:
                L[j] = max(L[j], L[i]+1)
    return max(L)


"""
Description: Implement computing number of longest subsequences
"""
def LNDS(seq, s):
    maxL = longestDistance(seq)
    graph = makeGraph(seq)
    n = len(seq)

    L = [None]*n
    for i in range(n):
        L[i] = [0,1] # length and count

    for v in range(n):
        if graph[v] == None:
            continue
        for u in graph[v]:
            if seq[u] >= seq[v]:
                if L[v][0] >= L[u][0]:
                    L[u][0] = L[v][0]+1
                    L[u][1] = L[v][1]
                elif L[v][0] == L[u][0]-1:
                    L[u][1] += L[v][1]

    toReturn = 0
    for i in range(n):
        if L[i][0] == maxL:
            toReturn += L[i][1]

    return toReturn % 20170429


if __name__ == '__main__':
    main()