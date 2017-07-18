import sys
from collections import deque

def floodfill(grid, yi, xi, h, w):
    stack = set(((yi, xi),))
    while stack:
        yi, xi = stack.pop()
        grid[yi][xi] = 0
        # print (yi, xi)
        if xi-1 >= 0 and grid[yi][xi-1] == 1:
            stack.add((yi, xi-1))
        if xi+1 < w and grid[yi][xi+1] == 1:
            stack.add((yi, xi+1))
        if xi-1 >= 0 and yi-1 >= 0 and grid[yi-1][xi-1] == 1:
            stack.add((yi-1, xi-1))
        if yi-1 >= 0 and grid[yi-1][xi] == 1:
            stack.add((yi-1, xi))
        if yi-1 >= 0 and xi+1 < w and grid[yi-1][xi+1] == 1:
            stack.add((yi-1, xi+1))
        if yi+1 < h and xi-1 >= 0 and grid[yi+1][xi-1] == 1:
            stack.add((yi+1, xi-1))
        if yi+1 < h and grid[yi+1][xi] == 1:
            stack.add((yi+1, xi))
        if yi+1 < h and xi+1 < w and grid[yi+1][xi+1] == 1:
            stack.add((yi+1, xi+1))


numOfTests = int(sys.stdin.readline())

# Data preprocessing
# Generate a grid
for i in range(numOfTests):
    inputs = sys.stdin.readline().split()
    h, w = map(int, inputs)
    grid = [None]*h
    for yi in range(h):
        xs = sys.stdin.readline().split()
        xs = map(int, xs)
        grid[yi] = xs

    count = 0
    for yi in range(h):
        for xi in range(w):
            if grid[yi][xi] == 1:
                # Flood fill
                floodfill(grid, yi, xi, h, w)
                # print grid
                count += 1

    print count