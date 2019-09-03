
class vertex:
	def __init__(self,u,v,wi):
		self.u=u
		self.v=v
		self.wi=wi
		

class Graph:
	def __init__(self,n):
		self.V=[[] for i in range(n)]
		self.V1=[float("infinity") for i in range(n)]
		self.vis=[False for i in range(n)]
		self.T=[]
		self.par=[None for i in range(n)]

	def addEdge(self,u,v,wi):
		self.V[u].append(vertex(u,v,wi))
		self.V[v].append(vertex(v,u,wi))

	def minimum(self):
		key=float("infinity")
		t=0
		for i in range(len(self.V1)):
			if self.V1[i]<key and self.vis[i]==False:
				key=self.V1[i]
				index=i
				t=1
		if t==1:
			return index
		else:
			print("Hi")
	def prims(self,u):
		self.V1[u]=0
		for i in range(len(self.V)):
			u=self.minimum()
			self.T.append(u)
			self.vis[u]=True
			for j in self.V[u]:
				if self.vis[j.v]==False and self.V1[j.v]>j.wi and j.wi>0:
					self.V1[j.v]=j.wi
					self.par[j.v]=u

	def prin(self):
		print("Edges are:",self.T)
		for i in self.T:
			if self.par[i]!=None:
				print(i,"-",self.par[i])

n=int(input("Enter number of node:"))
ed=int(input("Enter no of edges:"))
g=Graph(n)
for i in range(ed):
	arr=list(map(int,input().rstrip().split()))
	g.addEdge(arr[0],arr[1],arr[2])
e=int(input("Enter first node:"))
g.prims(e)
g.prin()
