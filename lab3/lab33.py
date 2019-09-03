def submax(arr):
	maxfi=ma=0
	r=[]
	j=k=-1
	for i in range(len(arr)):
		if ma==0:
			j=i
		ma+=arr[i]
		if ma<0:
			ma=0
		if ma>maxfi:
			k=i
			maxfi=ma
			r=[maxfi,j,k]
	return r
arr=list(map(int,input("Enter:").rstrip().split()))
r=submax(arr)
print("Ans:",r[0])
print("i:",r[1],",j:",r[2])