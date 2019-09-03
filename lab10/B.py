n=int(input("Enter number of vertices:"))
e=int(input("Enter number of Edges:"))
class Graph:
	def __init__(self,n):
		self.n=n
		self.V=[[] for i in range(n)]
		
	def addEdge(self,u,v,wi):
		self.V[u].append((u,v,wi))

T=[[float("infinity") for j in range(n)] for i in range(n)]
g=Graph(n)
print("Enter Edges:")
for i in range(e):
	arr=list(map(int,input().rstrip().split()))
	g.addEdge(arr[0],arr[1],arr[2])


s=int(input("Enter source node:"))
T[s][0]=0

res=[[] for i in range(n)]
res[0].append(s)
for j in range(n-1):
	for i in range(n):
		T[i][j+1]=T[i][j]
	for i in res[j]:
		for k in g.V[i]:
			if T[k[1]][j]>T[i][j]+k[2]:
				T[k[1]][j+1]=T[i][j]+k[2]
				#T[k[1]][j]=T[i][j]+k[2]
				res[j+1].append(k[1])

for i in res[n-1]:
	for k in g.V[i]:
		if T[k[1]][n-1]>T[i][n-1]+k[2]:
			print("The Graph contains negative weighted cycle!!")
			exit(0)

print(T)
for i in T:
	for j in i:
		if j==float("infinity"):
			print("- ",end=" ")
		else:
			print(j,end=" ")
	print()





