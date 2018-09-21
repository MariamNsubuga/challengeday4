numList=[] #initializing an empty list
def sumlist(numList):
	total=0 # initializing total=0
	for i in numList:
		if isinstance(i,list): # checking if there is a nested list
			total +=sumlist(i)
		else:
			total+=i
			
	return total
print(sumlist([1,3,5,[2,4,6],9]))