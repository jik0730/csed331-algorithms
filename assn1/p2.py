import sys

def ingyoSortAndStdOut(ilist):
    rlist = []
    while(len(ilist) != 0):
        # Search smallest
        smallest = sys.maxint
        sindex = 0
        for i in range(len(ilist)):
            if ilist[i] < smallest:
                smallest = ilist[i]
                sindex = i
        # Remove smallest from ilist
        del ilist[sindex]
        # Append smallest to rlist
        rlist.append(str(smallest))

    # Stdout
    for r in range(len(rlist)):
        if r != len(rlist)-1:
            sys.stdout.write(rlist[r]+" ")
        else:
            sys.stdout.write(rlist[r]+"\n")


numOfTests = sys.stdin.readline()

for i in range(int(numOfTests)):
    numOfElements = int(sys.stdin.readline())
    ilist = sys.stdin.readline().split()
    ilist = map(int, ilist)
    ingyoSortAndStdOut(ilist)
