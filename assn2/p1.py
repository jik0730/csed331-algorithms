import sys

def ingyoPow(n, k, m):
    if k == 1:
        return n%m
    elif n == 1:
        return 1
    elif n == 0 and k == 0:
        return 1
    elif n == 0:
        return 0
    elif k == 0:
        return 1
    temp = ingyoPow(n, k/2, m)
    if k%2 == 0:
        return (temp*temp)%m
    else:
        return ((n)*temp*temp)%m

numOfTests = int(sys.stdin.readline())

for i in range(numOfTests):
    inputs = sys.stdin.readline().split()
    inputs = map(int, inputs)
    toReturn = ingyoPow(inputs[0], inputs[1], 20170317)
    sys.stdout.write(str(toReturn)+"\n")

