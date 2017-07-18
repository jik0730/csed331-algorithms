import sys

def fib(n):
    if n == 0:
        return [0, 1]
    else:
        f1, f2 = fib(n // 2)
        f3 = (f1 * (f2 * 2 - f1)) % 20170317
        f4 = (f1 * f1 + f2 * f2) % 20170317
        if n % 2 == 0:
            return [f3, f4]
        else:
            return [f4, f3 + f4]


numOfTests = int(sys.stdin.readline())

while(numOfTests):
    numOfTests -= 1
    inputs = int(sys.stdin.readline())
    toReturn = fib(inputs)
    sys.stdout.write(str(toReturn[0]%20170317)+"\n")