arr=list(map(int,input().rstrip().split()))
T=[None for i in range(len(arr))]
T1=[None for i in range(len(arr))]


link=[None for i in range(len(arr))]
def diff(u,i):
	if arr[u]<arr[i]:
		return 1
	return 0
def memoPath(u):
	if T[u]!=None:
		return T[u]
	max=1
	for i in range(u+1,len(arr)):
		if 1+memoPath(i)>max:
			if arr[u]<arr[i]:
				max=1+memoPath(i)
	T[u]=max
	return T[u]

def Bottom():
	for i in range(len(arr)-1,-1,-1):
		max=1
		for j in range(i+1,len(arr)):
			if arr[i]<arr[j]:
				if 1+T1[j]>max:
					link[i]=j
					max=1+T1[j]
		T1[i]=max
	print(T1)
	return T1

memoPath(0)
print(T)
print("Ans:",max(T))
print("Ans:",max(Bottom()))
n=max(T1)
k=T1.index(max(T1))
r=link[k]
print(arr[k],end=" ")
while r!=None:
	print(arr[r],end=" ")
	r=link[r]
print()







