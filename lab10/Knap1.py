val=list(map(int,input().rstrip().split()))
wt=list(map(int,input().rstrip().split()))
val1=[0]+val
wt1=[0]+wt
W1=int(input("Enter total W:"))
T=[[None for j in range(W1+1)] for i in range(len(wt))]
T1=[[None for j in range(W1+1)] for i in range(len(wt)+1)]
for i in range(len(T1)):
	T1[i][0]=0
for j in range(W1+1):
	T1[0][j]=0

def Knap(W,wt,val,i):
	if W==0 or i==-1:
		return 0
	if T[i][W]!=None:
		return T[i][W]
	if wt[i]>W:
		T[i][W]=Knap(W,wt,val,i-1)
	else:
		T[i][W]=max(val[i]+Knap(W-wt[i],wt,val,i-1),Knap(W,wt,val,i-1))
	return T[i][W]

def Bottom():
	for j in range(1,W1+1):
		for i in range(1,len(T1)):
			if j<wt1[i]:
				T1[i][j]=T1[i-1][j]
			else:
			    T1[i][j]=max(val1[i]+T1[i-1][j-wt1[i]],T1[i-1][j])


print(Knap(W1,wt,val,len(wt)-1))
Bottom()
print(T1[len(wt)][W1])