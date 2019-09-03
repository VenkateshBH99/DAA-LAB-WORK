
def maximum(arr,l,h,mid):
	su=0
	left=-10000
	r=[]
	mi=-1
	ma=-1
	for i in range(mid,l-1,-1):
		su+=arr[i]
		if su>left:
			mi=i
			left=su
	su=0
	right=-1000
	for j in range(mid+1,h+1):
		su+=arr[j]
		if su>right:
			ma=j
			right=su
	r=[(left+right),mi,ma]
	return r


def m(r1,r2,r3):
	if r1[0]>r2[0]:
		if r1[0]>r3[0]:
			return r1
		else:
			return r3
	else:
		if r2[0]>r3[0]:
			return r2
		else:
			return r3

def maxsub(arr,l,h):
	if l==h:
		r=[arr[l],l,h]
		return r
	mid=(l+h)//2
	r1=maximum(arr,l,h,mid)
	r2=maxsub(arr,l,mid)
	r3=maxsub(arr,mid+1,h)
	return m(r1,r2,r3)
	#return max(maxsub(arr,l,mid),maxsub(arr,mid+1,h),r[0])

arr=list(map(int,input("Enter:").rstrip().split()))
r=maxsub(arr,0,len(arr)-1)
print("Ans:",r[0],"\ni:",r[1],",j:",r[2])