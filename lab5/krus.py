from set import DSU

def Krushkals(A,n):
	g=DSU(n)
	for i in range(n):
		g.makeSet(i)
	A.sort(key=lambda k:k[2])
	T=[]
	for i in range(len(A)):
		if g.findSet(A[i][0]).u!=g.findSet(A[i][1]).u:
			T.append([A[i][0],A[i][1]])
			g.union(A[i][0],A[i][1])
	return T

n=int(input("Enter no of nodes:"))
e=int(input("Enter no of Edges:"))
A=[]
for i in range(e):
	a=list(map(int,input().rstrip().split()))
	A.append(a)
R=Krushkals(A,n)
for i in R:
	print(i)


