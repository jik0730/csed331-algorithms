import sys

"""
Closest pair algorithm

Steps
1. Divide pair into two equally divided regions along x-axis.
2. For the base cases, if there are two points left, return the distance
between them, and if there is one point left, return max size of length.
3. Otherwise, 

""" 

"""
input(x,y): each is a list of two numbers representing x,y coordinate.
"""
def man(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])+abs(x[2]-y[2])


"""
input(nlist): sorted number list in x-axis
"""
def cpl(nlist):
    lsize = len(nlist)
    if lsize == 1:
        return sys.float_info.max
    elif lsize == 2:
        return man(nlist[0], nlist[1])

    half = int(lsize/2)
    leftChunk = nlist[0:half]
    rightChunk = nlist[half:lsize]

    leftDelta = cpl(leftChunk)
    rightDelta = cpl(rightChunk)
    minDelta = min(leftDelta, rightDelta)

    mid = (leftChunk[half-1][0]+rightChunk[0][0])/2

    leftList = []
    for i in range(half-1, -1, -1):
        if leftChunk[i][0] <= mid-minDelta:
            break
        leftList.append(leftChunk[i])
    # Break point
    if len(leftList) == 0:
        return minDelta

    rightList = []
    for i in range(0,len(rightChunk)):
        if rightChunk[i][0] >= mid+minDelta:
            break
        rightList.append(rightChunk[i])

    for e1 in leftList:
        # Break point
        if len(rightList) == 0:
            break
        xp = e1[0]
        yp = e1[1]
        zp = e1[2]
        for e2 in rightList:
            if yp-minDelta < e2[1] and e2[1] < yp+minDelta and zp-minDelta < e2[2] and e2[2] < zp+minDelta:
                distance = man(e1, e2)
                minDelta = min(minDelta, distance)

    return minDelta

numOfTests = int(sys.stdin.readline())

while(numOfTests):
    numOfTests -= 1
    numOfPoints = int(sys.stdin.readline())
    points = []
    while(numOfPoints):
        numOfPoints -= 1
        xyz = sys.stdin.readline().split()
        xyz = map(int, xyz)
        points.append(xyz)
    inputList = sorted(points, key=lambda point: point[0])
    closest = cpl(inputList)
    sys.stdout.write(str(closest)+"\n")

