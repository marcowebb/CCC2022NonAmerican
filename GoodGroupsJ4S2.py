pairList = []
divList = []
groupList = []
constraint = []

# pairs = must work together
# divorces = must be apart


# work together variable
numPairs = int(input())
for i in range(0, numPairs):
    a, b = [i for i in input().split()]
    pairList.append(a)
    pairList.append(b)
    constraint.append(1)


# work separate variable
numDivorces = int(input())
for i in range(0, numDivorces):
    a, b = [i for i in input().split()]
    divList.append(a)
    divList.append(b)
    constraint.append(1)


# group variable
numGroup = int(input())
for i in range(0, numGroup):
    a, b, c = [i for i in input().split()]
    groupList.append(a)
    groupList.append(b)
    groupList.append(c)


# confirm pairs first
for i in range(0, numGroup): 
    groupMemTemp = ["", "" ,""]
    groupMemTemp[0] = groupList[(i * 3)]
    groupMemTemp[1] = groupList[(i * 3) + 1]
    groupMemTemp[2] = groupList[(i * 3) + 2]
    for o in range(0, numPairs):
        check0 = False
        check1 = False
        pairMem0 = pairList[(o * 2)]
        pairMem1 = pairList[(o * 2) + 1]
        for p in range(0, 3):
            if groupMemTemp[p] == pairMem0:
                check0 = True
            elif groupMemTemp[p] == pairMem1:
                check1 = True
        
        if check0 == True and check1 == False:
            constraint[o] = 0
        elif check0 == False and check1 == True:
            constraint[o] = 0


# confirm divorces next
for i in range(0, numGroup): 
    groupMemTemp = ["", "" ,""]
    groupMemTemp[0] = groupList[(i * 3)]
    groupMemTemp[1] = groupList[(i * 3) + 1]
    groupMemTemp[2] = groupList[(i * 3) + 2]
    for o in range(0, numDivorces):
        check0 = False
        check1 = False
        divMem0 = divList[(o * 2)]
        divMem1 = divList[(o * 2) + 1]
        for p in range(0, 3):
            if groupMemTemp[p] == divMem0:
                check0 = True
            elif groupMemTemp[p] == divMem1:
                check1 = True
        
        if check0 == True and check1 == True:
            constraint[o + numPairs] = 0

# count violations
violations = 0
for i in range(0, len(constraint)):
    if constraint[i] == 0:
        violations += 1
print(violations)