def peak(arr,l,h,n):
	mid=l+(h-l)/2
	mid=int(mid)
	if((mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid])):
		return mid

	elif mid>0 and arr[mid-1]>arr[mid]:
		return peak(arr,l,mid-1,n)

	else:
		return peak(arr,mid+1,h,n)

w=input("Enter:")
arr=list(map(int,w.rstrip().split()))
print(arr[peak(arr,0,len(arr)-1,len(arr))])

