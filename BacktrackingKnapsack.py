# //Example input
# numberOfItems = 5
# knapsackCapacity = 10
# weights = [2, 2, 6, 5, 4]
# values = [6, 3, 5, 4, 6]
# selectionList = [False for i in range(numberOfItems)]

numberOfItems = int(input("number of items : "))
knapsackCapacity = int(input("knapsack capacity : "))
weights = [int(input(f"weight {i} : ")) for i in range(1,numberOfItems+1) ]
values = [int(input(f"value {i} : ")) for i in range(1,numberOfItems+1)]
selectionList = [False for i in range(numberOfItems)]

currentWeight = 0
currentValue = 0
bestV = 0

def backtrack(i):
    global bestV, currentWeight, currentValue, selectionList, chosenItems
    if i >= numberOfItems:
        if bestV < currentValue:
            bestV = currentValue
            chosenItems = selectionList[:]
    else:
        if currentWeight + weights[i] <= knapsackCapacity:
            selectionList[i] = True
            currentWeight += weights[i]
            currentValue += values[i]
            backtrack(i + 1)
            currentWeight -= weights[i]
            currentValue -= values[i]
        selectionList[i] = False
        backtrack(i + 1)

backtrack(0)
print("optimal value : ",bestV)
print("chosen items : ",chosenItems)