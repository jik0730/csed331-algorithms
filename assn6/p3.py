import sys


def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        s = int(sys.stdin.readline())
        seq = map(int, sys.stdin.readline().split())
        print(LBS(seq, s))
        numOfTests -= 1


"""
Description: Make two version of graph representation(upward, downward)
"""
def makeGraph(seq):
    n = len(seq)
    graph = [None]*n
    for v1 in range(n):
        for v2 in range(v1+1, n):
            if seq[v2] > seq[v1]:
                if graph[v1] == None:
                    graph[v1] = [v2]
                else:
                    graph[v1].append(v2)
    graph2 = [None]*n
    dseq = seq[::-1]
    for v1 in range(n):
        for v2 in range(v1+1, n):
            if dseq[v2] > dseq[v1]:
                if graph2[v1] == None:
                    graph2[v1] = [v2]
                else:
                    graph2[v1].append(v2)
    return graph, graph2


"""
Description: Compute length of longest bitonic subsequence
"""
def longestBitonicDistance(seq):
    L_i = _longestIncreasingSubseq(seq)
    L_d = _longestDecreasingSubseq(seq)
    L = [L_i[i]+L_d[i] for i in range(len(L_i))]
    return max(L)


"""
Description: Compute increasing longest subsequence
"""
def _longestIncreasingSubseq(seq):
    n = len(seq)
    L = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if seq[j] > seq[i]:
                L[j] = max(L[j], L[i]+1)
    return L


"""
Description: Compute decreasing longest subsequence
"""
def _longestDecreasingSubseq(seq):
    n = len(seq)
    dseq = seq[::-1]
    L = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if dseq[j] > dseq[i]:
                L[j] = max(L[j], L[i]+1)
    return L[::-1]


"""
Description: Implement computing number of longest increasing subsequences
"""
def i_LNDS(seq, graph):
    n = len(seq)

    L = [None]*n
    for i in range(n):
        L[i] = [0,1] # length and count

    for v in range(n):
        if graph[v] == None:
            continue
        for u in graph[v]:
            if seq[u] > seq[v]:
                if L[v][0] >= L[u][0]:
                    L[u][0] = L[v][0]+1
                    L[u][1] = L[v][1]
                elif L[v][0] == L[u][0]-1:
                    L[u][1] += L[v][1]

    return L


"""
Description: Implement computing number of longest decreasing subsequences
"""
def d_LNDS(seq, graph):
    n = len(seq)
    dseq = seq[::-1]

    L = [None]*n
    for i in range(n):
        L[i] = [0,1] # length and count

    for v in range(n):
        if graph[v] == None:
            continue
        for u in graph[v]:
            if dseq[u] > dseq[v]:
                if L[v][0] >= L[u][0]:
                    L[u][0] = L[v][0]+1
                    L[u][1] = L[v][1]
                elif L[v][0] == L[u][0]-1:
                    L[u][1] += L[v][1]

    return L[::-1]


"""
Description: Compute number of longest biotic subsequences
"""
def LBS(seq, s):
    maxLB = longestBitonicDistance(seq)
    iGraph, dGraph = makeGraph(seq)
    iL = i_LNDS(seq, iGraph)
    dL = d_LNDS(seq, dGraph)
    
    toReturn = 0
    for i in range(s):
        if iL[i][0] + dL[i][0] == maxLB:
            toReturn += iL[i][1] * dL[i][1]

    return toReturn % 20170429


if __name__ == '__main__':
    main()