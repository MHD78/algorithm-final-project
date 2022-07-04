# //Example input
# numberOfItems = 5
# knapsackCapacity = 10
# weights = [2, 2, 6, 5, 4]
# values = [6, 3, 5, 4, 6]
# itemsInit = [0 for i in range(numberOfItems)]

numberOfItems = int(input("number of items : "))
knapsackCapacity = int(input("knapsack capacity : "))
weights = [int(input(f"weight {i} : ")) for i in range(1,numberOfItems+1) ]
values = [int(input(f"value {i} : ")) for i in range(1,numberOfItems+1)]
itemsInit = [False for i in range(numberOfItems)]

optP = 0
optX=[]

def backtrackKnapsack(X,l):
	global optP	, optX
	if l == numberOfItems:
		if sum([X[i] * weights[i] for i in range(0,numberOfItems)]) <= knapsackCapacity:
			currP = sum([X[i] * values[i] for i in range(0,numberOfItems)])
			if currP >= optP :
				optP = currP
				optX = X[:]
	else:
		X[l]=1
		backtrackKnapsack(X,l+1)
		X[l]=0
		backtrackKnapsack(X,l+1)

backtrackKnapsack(itemsInit,0)
print("Optimal Value : ", optP)
print("Selected Objects : ",optX)