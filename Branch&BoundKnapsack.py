#  //Example input
# numberOfItems = 5
# knapsackCapacity = 10
# weights = [2, 2, 6, 5, 4]
# values = [6, 3, 5, 4, 6]
# itemsInit = [0 for i in range(numberOfItems)]

numberOfItems = int(input("number of items : "))
knapsackCapacity = int(input("knapsack capacity : "))
weights = [int(input(f"weight {i} : ")) for i in range(1,numberOfItems+1) ]
values = [int(input(f"value {i} : ")) for i in range(1,numberOfItems+1)]
itemsInit = [0 for i in range(numberOfItems)]

currW = 0
currV = 0
optP = 0
optX=[]

def branchAndBoundBacktrack(i):
    global optP, currW, currV, itemsInit, optX
    if i == numberOfItems:
        if optP < currV:
            optP = currV
            optX = itemsInit[:]
    else:
        if currW + weights[i] <= knapsackCapacity:
            itemsInit[i] = 1
            currW += weights[i]
            currV += values[i]
            branchAndBoundBacktrack(i + 1)
            currW -= weights[i]
            currV -= values[i]
        itemsInit[i] = 0
        branchAndBoundBacktrack(i + 1)

branchAndBoundBacktrack(0)
print("optimal value : ",optP)
print("chosen items : ",optX) 