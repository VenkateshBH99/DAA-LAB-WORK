def zero(arr):
	i=0
	j=len(arr)-1
	r=[]
	while arr[i]<=0 and arr[j]>=0 and i!=j:
		if arr[i]+arr[j]==0:
			r.append([arr[i],arr[j]])
			if arr[i]==0 and arr[j]==0:
				break
			i+=1
			j-=1
		elif (-arr[i])>arr[j]:
			i+=1
		elif (-arr[i])<arr[j]:
			j-=1
	return r




arr=list(map(int,input("Enter:").rstrip().split()))
arr.sort()
print(arr)
print(zero(arr))