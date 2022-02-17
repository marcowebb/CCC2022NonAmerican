regularCount = int(input())
smallCount = int(input())
totalCount = 0
leftover = 0

totalCount += regularCount * 8
totalCount += smallCount * 3

leftover = totalCount - 28

print(leftover)