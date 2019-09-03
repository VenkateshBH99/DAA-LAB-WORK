def maxi(arr,r,c,ma):
	max_i=0
	for i in range(len(arr)):
		if ma<arr[i][c]:
			ma=arr[i][c]
			#print(ma)
			max_i=i
	return max_i

def peakrec(arr,r,c,mid):
	ma=0
	max_i=maxi(arr,r,mid,ma)
	if mid==0 or mid==c-1:
		return arr[max_i][mid]

	if arr[max_i][mid]>=arr[max_i][mid-1] and arr[max_i][mid]>=arr[max_i][mid+1]:
		return arr[max_i][mid]

	if arr[max_i][mid-1]>arr[max_i][mid]:
		return peakrec(arr,r,c,mid-(mid//2))
	return peakrec(arr,r,c,mid+(mid//2))

def findpeak(arr,r,c):
	return peakrec(arr,r,c,(c//2))

n=int(input("Enter n:"))
arr=[]
for i in range(n):
	arr.append(list(map(int,input().rstrip().split())))
print("peak:",findpeak(arr,len(arr),len(arr)))