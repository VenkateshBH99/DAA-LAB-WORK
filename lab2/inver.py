def merge(arr):
	c=0
	if len(arr)>1:
		mid=len(arr)//2
		L=arr[:mid]
		R=arr[mid:]
		c=merge(L)
		c+=merge(R)
		c+=count(L,R,arr)
	return c
def count(L,R,arr):
	i=j=k=0
	c=0
	while i<len(L) and j<len(R):
		if L[i]<R[j]:
			arr[k]=L[i]
			i+=1
		else:
			arr[k]=R[j]
			j+=1
			c+=len(L)-i
		k+=1
	while i<len(L):
		arr[k]=L[i]
		k+=1
		i+=1
	while j<len(R):
		arr[k]=R[j]
		j+=1
		k+=1
	return c

n=input("Enter:")
arr=list(map(int,n.rstrip().split()))
print(merge(arr))
