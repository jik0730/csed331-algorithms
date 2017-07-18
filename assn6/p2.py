import sys

numOfTests = int(sys.stdin.readline())

while numOfTests:
    n, m = map(int, sys.stdin.readline().split())
    if (n%4==0 and m%4==0) or (n%4==1 and m%4==1) or (n%4==2 and m%4==2) or (n%4==3 and m%4==3):
        print('B')
    else:
        print('A')
    numOfTests -= 1