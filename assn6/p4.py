import sys


def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        n, m = map(int, sys.stdin.readline().split())
        print(minCutting(n, m))
        numOfTests -= 1


def minCutting(n, m):
    if n == 1:
        return m-1
    return minCutting(int(n/2), m) + minCutting(n-int(n/2), m) + 1


if __name__ == '__main__':
    main()