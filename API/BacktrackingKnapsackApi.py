optP = 0
optX=[]

def backtrackKnapsack(X,numberOfItems,weights,values,knapsackCapacity,l):
	global optP	, optX
	if l == numberOfItems:
		if sum([X[i] * weights[i] for i in range(0,numberOfItems)]) <= knapsackCapacity:
			currP = sum([X[i] * values[i] for i in range(0,numberOfItems)])
			if currP >= optP :
				optP = currP
				optX = X[:]
	else:
		X[l]=1
		backtrackKnapsack(X,numberOfItems,weights,values,knapsackCapacity,l+1)
		X[l]=0
		backtrackKnapsack(X,numberOfItems,weights,values,knapsackCapacity,l+1)

def resultHandler(n,k,w,v):
    numberOfItems = n
    itemsInit = [0 for i in range(numberOfItems)]
    backtrackKnapsack(itemsInit,n,w,v,k,0)
    result = {"Optimal Value":optP , "Selected Objects":optX}
    return result
    
