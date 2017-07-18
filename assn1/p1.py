import sys

numOfTests = sys.stdin.readline()

for i in range(int(numOfTests)):
    A, B = sys.stdin.readline().split()
    C = int(A) + int(B)
    sys.stdout.write(str(C)+"\n")