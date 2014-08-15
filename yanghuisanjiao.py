NUM = 6
 
def printLine(lineList):
    lineList = [str(tmpNum) for tmpNum in lineList]
    print("%s %s" % (" " * (NUM - len(lineList)), " ".join(lineList)))
 
for i in range(NUM):
    if i < 2:
        yhList = [1] * (i + 1)
    else:
        yhList[1:-1] = [(tmpNum + yhList[j]) for j, tmpNum in enumerate(yhList[1:])]
    printLine(yhList)
