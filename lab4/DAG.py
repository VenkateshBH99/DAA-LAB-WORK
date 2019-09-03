
class C:
	def __init__(self,v):
		self.v=v
		self.cour=0
		self.count=0

class Graph:
	def __init__(self,n):
		self.n=n
		self.V=[[] for i in range(n)]
		self.V1=[C(i) for i in range(n)]
		self.Course=[]

	def addEdge(self,u,v):
		self.V[u].append(v)
		self.V1[v].count+=1

	def Topological(self):
		S=[]
		j=0
		print("Courses   sem")
		for i in self.V1:
			if i.count==0:
				i.cour=+1
				S.append(i.v)
				
		while S:
			u=S.pop(0)
			print(u,'     ',self.V1[u].cour)
			for i in self.V[u]:
				self.V1[i].count-=1
				if self.V1[i].count==0:
					self.V1[i].cour=self.V1[u].cour+1
					S.append(i)


n=int(input("Enter number of nodes:"))
e=int(input("Enter number of edges"))
print("Enter:")
g=Graph(n)
for i in range(e):
	a=list(map(int,input().rstrip().split()))
	g.addEdge(a[0],a[1])
print("Ans:")
g.Topological()

