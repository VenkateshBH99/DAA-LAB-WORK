class m:
	def __init__(self):
		self.ma=0
		self.v=None

class node:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None
		self.count=1
		self.height=1


	def insert(self,root,val,m):
		if root==None:
			return node(val)
		elif val==root.val:
			if val==root.val:
				root.count+=1
				if root.count>m.ma:
					m.ma=root.count
					m.v=val
			return root
		elif val<root.val:
			root.left=self.insert(root.left,val,m)
		else:
			root.right=self.insert(root.right,val,m)

		root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
		balance=self.getBalance(root)
		if balance>1 and val<=root.left.val:
			return self.rightRotate(root)

		if balance<-1 and val>root.right.val:
			return self.leftRotate(root)

		if balance>1 and val>root.left.val:
			root.left=self.leftRotate(root.left)
			return self.rightRotate(root)

		if balance<-1 and val<=root.right.val:
			root.right=self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def rightRotate(self,z):
		y=z.left
		T3=y.right

		y.right=z
		z.left=T3

		z.heigth=1+max(self.getHeight(z.left),self.getHeight(z.right))
		y.heigth=1+max(self.getHeight(y.left),self.getHeight(y.right))
		return y

	def leftRotate(self,z):
		y=z.right
		print(z.val)
		T3=y.left

		y.left=z
		z.right=T3

		z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
		y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))
		return y

	def getHeight(self,root):
		if root==None:
			return 0
		return root.height

	def getBalance(self,root):
		if root==None:
			return 0
		return self.getHeight(root.left)-self.getHeight(root.right)


arr=list(map(int,input("Enter:").rstrip().split()))

r=None
g=node(None)
m=m()
for i in arr:
	r=g.insert(r,i,m)
if m.ma>len(arr)//2:
	print(m.v)
else:
	print("No")

