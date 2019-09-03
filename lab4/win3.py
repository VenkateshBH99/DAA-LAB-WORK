class p:
	def __init__(self,v):
		self.v=v
		self.count=0

class hash:
	def __init__(self,n):
		self.A=[p(None) for i in range(n)]

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
			return [True,i]
		return [False,i]

A=list(map(int,input("Enter:").rstrip().split()))
g=hash(len(A))
for i in A:
	r=g.add(i)
	if r[0]==True:
		break
if r[0]==False:
	print("No Majority")
else:
	print(r[1])

