n=int(input("Enter the number of intervals:"))
arr=[]
for i in range(n):
	arr.append(list(map(int,input().rstrip().split())))
arr.sort(key=lambda k:k[1])
T=[]
r=0
for i in range(len(arr)):
	if r==0:
		r=1
		T.append(arr[i])
	else:
		if T[len(T)-1][1]<=arr[i][0]:
			T.append(arr[i])
print("max:",len(T),"process that is:")
print(T)

