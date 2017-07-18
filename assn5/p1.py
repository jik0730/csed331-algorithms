import sys
from collections import deque


"""
Description: Main function
"""
def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        # Take inputs representing information to use
        numV = int(sys.stdin.readline())
        inputs = sys.stdin.readline().split()
        edges = deque(map(int, inputs))

        # Test a tree as perfect matching
        perfectMatching(edges, numV)

        numOfTests -= 1


"""
Description: Check whether a tree is perfect matching or not
Input: graph
Output: boolean
"""
def perfectMatching(edges, numV):
    visited = set()
    V = set()
    numOfVertices = numV
    # Iterate edges
    while len(edges) != 0:
        u = numV
        v = edges.pop()
        if u not in V and v not in V:
            V.add(u)
            V.add(v)
        numV -= 1
        
    if len(V) == numOfVertices:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()