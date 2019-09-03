n=int(input("Enter the number of nodes:"))
G=[[] for i in range(n)]
GR=[[] for i in range(n)]
e=int(input("Enter number of edges:"))
for i in range(e):
	arr=list(map(int,input().rstrip().split()))
	G[arr[0]].append(arr[1])
	GR[arr[1]].append(arr[0])
for i in G:
	i.sort()
for i in GR:
	i.sort()
class prop:
	def __init__(self,u):
		self.u=u
		self.flag=False
		self.t1=-1
		self.t2=-1
class DFS:
	def __init__(self,G):
		self.graph=[]
		for i in G:
			self.graph.append(i)
		self.V=[prop(i) for i in range(len(G))]
		self.T=[]
		self.time=-1

	def dfs(self,u):
		self.V[u].flag=True
		self.time+=1
		self.V[u].t1=self.time
		for i in self.graph[u]:
			if self.V[i].flag==False:
				self.dfs(i)	

		self.time+=1
		self.V[u].t2=self.time
		self.T.append([self.V[u].t1,self.V[u].t2,u])

gr=DFS(GR)
for i in range(len(gr.V)):
	if gr.V[i].flag==False:
		gr.dfs(i)

gr.T.sort(key=lambda k:k[1])
while gr.T:
	q=gr.T.pop()
	g=DFS(G)
	g.dfs(q[2])
	print(g.T)
	for i in range(len(g.T)-1):
		gr.T.pop()
	for i in range(len(G)):
		for j in range(len(g.T)):
			if g.T[j][2] in G[i]:
				ind=G[i].index(g.T[j][2])
				G[i].pop(ind)
			
	print()







