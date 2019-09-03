class p:
	def __init__(self,v):
		self.v=v
		self.count=0

class hash:
	def __init__(self,n):
		self.A=[p(None) for i in range(n)]
		self.r=None

	def add(self,i):
		k=i%len(self.A)
		while self.A[k].v!=None and self.A[k].v!=i:
			k=(k+1)%n
		if self.A[k].v==None:
			self.A[k].v=i
			self.A[k].count+=1
		elif self.A[k].v==i:
			self.A[k].count+=1
		if self.A[k].count>len(self.A)//2:
			self.r=i

def divide(g,arr):
	if len(arr)==1:
		return g.add(arr[0])
	mid=len(arr)//2
	left=arr[:mid]
	right=arr[mid:]
	divide(g,left)
	divide(g,right)

arr=list(map(int,input("Enter:").rstrip().split()))
g=hash(len(arr))
divide(g,arr)
if g.r==None:
	print("No majority")
else:
	print(g.r)

