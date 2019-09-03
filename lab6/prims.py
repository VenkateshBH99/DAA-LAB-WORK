import heapq as heapq
class ver:
	def __init__(self,u,v,w):
		self.u=u
		self.v=v
		self.w=w
class Graph:
	def __init__(self,n):
		self.V=[[] for i in range(n)]
		self.V1=[float("infinity") for i in range(n)]
		self.pre=[None for i in range(n)]
		self.T=[]

	

	def addEdge(self,u,v,w):
		self.V[u].append(ver(u,v,w))
		self.V[v].append(ver(v,u,w))

	def prims(self,s):
		self.V1[s]=0
		key=[False for i in range(len(self.V))]
		
		
		h=[]
		for i in range(len(self.V)):
			heapq.heappush(h,(self.V1[i],i))

		while h:
			u=heapq.heappop(h)[1]
			print(u)
			key[u]=True
			self.T.append(u)
			for j in self.V[u]:
				if j.w<self.V1[j.v] and key[j.v]==False:
					self.V1[j.v]=j.w
					self.pre[j.v]=u
					for i in range(len(h)):
						if h[i][1]==j.v:
							h[i]=(j.w,j.v)
							break
					heapq.heapify(h)
					

	def prin(self):
		for i in range(len(self.V)):
			if self.pre[i]!=None:
				print(i,"-",self.pre[i],":",self.V1[i])

n=int(input("Enter no of nodes:"))
e=int(input("Enter no of edges:"))
g=Graph(n)
for i in range(e):
	arr=list(map(int,input().rstrip().split()))
	g.addEdge(arr[0],arr[1],int(arr[2]))

s=int(input("Enter start node:"))
g.prims(s)
g.prin()
		
