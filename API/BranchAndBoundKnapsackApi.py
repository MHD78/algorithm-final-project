currW = 0
currV = 0
optP = 0
optX=[]

def branchAndBoundBacktrack(itemsInit,numberOfItems,weights,values,knapsackCapacity,i):
    global optP, currW, currV, optX
    if i == numberOfItems:
        if optP < currV:
            optP = currV
            optX = itemsInit[:]
    else:
        if currW + weights[i] <= knapsackCapacity:
            itemsInit[i] = 1
            currW += weights[i]
            currV += values[i]
            branchAndBoundBacktrack(itemsInit,numberOfItems,weights,values,knapsackCapacity,i + 1)
            currW -= weights[i]
            currV -= values[i]
        itemsInit[i] = 0
        branchAndBoundBacktrack(itemsInit,numberOfItems,weights,values,knapsackCapacity,i + 1)

def bresultHandler(n,k,w,v):
    numberOfItems = n
    itemsInit = [0 for i in range(numberOfItems)]
    branchAndBoundBacktrack(itemsInit,n,w,v,k,0)
    result = {"Optimal Value":optP , "Selected Objects":optX}
    return result