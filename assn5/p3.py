import sys


"""
Description: Main function
"""
def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        # Inputs
        n, k = map(int, sys.stdin.readline().split())

        # Make graph and data structures
        graph = makeGraph(n)
        K, D = dataPreprocessing(graph, n)

        # Algorithm, return list of students
        students = findStudents(graph, K, D, n, k)

        # Print statement
        print(len(students))

        numOfTests -= 1


"""
Description: Find best set of students who can be invited
Inputs: K, D, n
Output: List of students
"""
def findStudents(g, K, D, n, k):
    students = set()
    students.update(range(n))

    while True:
        I = set()
        for i in students:
            if K[i] < k or D[i] < k:
                _update(g, K, D, i)
                I.add(i)
        if len(I) == 0:
            break
        else:
            students -= I

    return students


"""
Description: Internal function on updating K, D
"""
def _update(g, K, D, i):
    for j in range(len(g)):
        if g[i][j] == 1:
            K[j] -= 1
        else:
            D[j] -= 1

    
"""
Description: Make K, D lists from input data
Output: K, D
"""
def dataPreprocessing(g, n):
    K = [None]*n
    D = [None]*n
    for i in range(n):
        data = g[i]
        kCount = 0
        for j in range(len(data)):
            if data[j] == 1:
                kCount += 1
        K[i] = kCount
        D[i] = n - kCount - 1
    return K, D


"""
Description: To make a graph representation(matrix)
Input: Number of vertices(int), edges(int)
Output: An adjacency list of the graph(list of list)
"""
def makeGraph(numV):
    graph = []
    while numV:
        graph.append(map(int, sys.stdin.readline().split()))
        numV -= 1
    return graph


if __name__ == '__main__':
    main()