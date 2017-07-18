import sys

def ingyoQuickSort(ilist):
    # Stop condition
    if len(ilist) <= 1:
        return ilist

    pivot = ilist[0]
    less = []
    equal = []
    more = []

    for i in ilist:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)

    return ingyoQuickSort(less) + equal + ingyoQuickSort(more)


def ingyoStdOut(rlist):
    # Stdout
    for r in range(len(rlist)):
        if r != len(rlist)-1:
            sys.stdout.write(str(rlist[r])+" ")
        else:
            sys.stdout.write(str(rlist[r])+"\n")


numOfTests = int(sys.stdin.readline())

for i in range(numOfTests):
    numOfElements = int(sys.stdin.readline())
    ilist = sys.stdin.readline().split()
    ilist = map(int, ilist)
    ilist = ingyoQuickSort(ilist)
    ingyoStdOut(ilist)

