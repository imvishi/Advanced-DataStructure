#BinaryIndexedTree update elements and calculate prefix sums in a array of numbers.
##complexity O(nlogn) 
def getSum(BITTree,i):
	s=0
	while i>0:
		s+=BITTree[i]
		i=i&(i-1)
		##or  i-=i&(-i)
	return s
def updatebit(BITTree,n,i,v):
	i+=1
	while i<=n:
		#print i,		
		BITTree[i]+=v
		i+=i&(-i)

def construct(arr,n):
	BITTree=[0 for i in range(n+1)]
	for i in range(n):
		updatebit(BITTree,n,i,arr[i])
	return BITTree
array=[2,1,1,3,2,3,4,5,6,7,8,9]
BITTree=construct(array,len(array))
print ("BITTree is",BITTree)
print ("array is",array)
print getSum(BITTree,5)
array[3]=0
updatebit(BITTree,len(array),3,-3)
print getSum(BITTree,5)
print ("BITTree is",BITTree)
print ("array is",array)

