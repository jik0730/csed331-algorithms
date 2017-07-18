import sys


"""
Description: Main function
"""
def main():
    numOfTests = int(sys.stdin.readline())

    while numOfTests:
        # Data preprocessing
        info = []
        D, n = map(int, sys.stdin.readline().split())
        d, p = map(int, sys.stdin.readline().split())
        for i in range(n-1):
            d2, p2 = map(int, sys.stdin.readline().split())
            info.append((p, d2-d))
            d = d2
            p = p2
        info.append((p, D-d))

        # Perform the algorithm and print output
        print(cost(n, info))

        numOfTests -= 1


"""
Description: Cost function in dynamic programming
Inputs: k(number of length), p(gradient of price-list)
"""
def cost(k, info):
    cost = 0
    p = info[0][0]
    for k in range(len(info)):
        if p > info[k][0]:
            p = info[k][0]
        cost = cost + (p*info[k][1])
    return cost


if __name__ == "__main__":
    main()