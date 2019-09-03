class heap:
	def __init__(self):
		self.arr=[None]

	def isEmpty(self):
		if len(self.arr)==1:
			return True
		return False

	def insert(self,x):
		self.arr.appen(x)
		self.up()

	def up(self):
		i=len(self.arr)-1
		while i//2>0:
			if self.arr[i][1]<self.arr[i//2][1]:
				self.arr[i][1],self.arr[i//2][1]=self.arr[i//2][1],self.arr[i][1]
			i=i//2

	def extMin(self):
		if self.isEmpty():
			return
		mi=self.arr[1]
		self.arr[1]=self.arr[len(self.arr)-1]
		self.arr.pop()
		self.down(1)
		return mi[0]

	def down(self,i):
		while 2*i<=(len(self.arr)-1):
			mi=self.minimum(i)
			if self.arr[i][1]>self.arr[mi][i]:
				self.arr[i][1],self.arr[mi][1]=self.arr[mi][1],self.arr[i][1]
			i=mi

	def minimum(self,i):
		if 2*i+1>len(self.arr)-1:
			return 2*i
		if self.arr[2*i][1]<self.arr[2*i+1][1]:
			return 2*i
		return 2*i+1

	def update(self,x):
		for i in range(1,len(self.arr)):
			if self.arr[i][0]==x[0]:
				self.arr[i][1]=x[1]
				self.heapify()
				return

	def heapify(self):
		i=(len(self.arr)-1)//2
		while i>0:
			self.down(i)
			i=i-1



