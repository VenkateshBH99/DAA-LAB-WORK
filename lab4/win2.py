mdef findCandidate(A):
	ma_in=0
	count=1
	for i in range(len(A)):
		if A[ma_in]==A[i]:
			count+=1
		else:
			count-=1
		if count==0:
			ma_in=i
			count=1
	return A[ma_in]

def isMajority(A,cand):
	count=0
	for i in range(len(A)):
		if A[i]==cand:
			count+=1
	if count>len(A)/2:
		return True
	return False

arr=list(map(int,input("Enter:").rstrip().split()))
cand=findCandidate(arr)
if isMajority(arr,cand):
	print(cand)
else:
	print("No Majority element!!")

