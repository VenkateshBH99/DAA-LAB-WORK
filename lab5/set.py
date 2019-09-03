class List:
	def __init__(self,u):
		self.u=u
		self.parent=u
		self.rank=0

class DSU:
	def __init__(self,n):
		self.V=[-1 for i in range(n+1)]
		self.T=[]

	def makeSet(self,u):
		self.V[u]=List(u)
		self.T.append(u)

	def findSet(self,u):
		if self.V[u].parent!=u:
			q=self.findSet(self.V[u].parent)
			self.V[u].parent=q.u
			return q

		return self.V[u]

	def union(self,x,y):
		rx=self.findSet(x)
		ry=self.findSet(y)
		#print(ry.u)
		if rx.rank>ry.rank:
			ry.parent=rx.u
		elif rx.rank<ry.rank:
			rx.parent=ry.u
		else:
			ry.parent=rx.u
			rx.rank+=1

	def printSet(self):
		for i in self.T:
			print(self.V[i].u,"-",self.V[i].parent)

def main():
	n=int(input("Enter no of nodes:"))
	g=DSU(n)
	for i in range(n):
		g.makeSet(i+1)
	while True:
		ch=int(input("1.makeSet\n2.findSet\n3.union\n4.print Set\n5.exit\nEnter ur choice:"))
		if ch==1:
			a=int(input("Enter node:"))
			g.makeSet(a)
		elif ch==2:
			a=int(input("Enter:"))
			print("ans:",g.findSet(a).u)
		elif ch==3:
			ar=list(map(int,input("Enter:").rstrip().split()))
			g.union(ar[0],ar[1])
		elif ch==4:
			g.printSet()
		elif ch==5:
			break
		else:
			print("Wrong choice")
if __name__ == '__main__':
	main()



