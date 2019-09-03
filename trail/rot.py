class ListNode:
	def __init__(self,val):
		self.val=val
		self.next=None

class R:
	def __init__(self):
		self.head=None
		self.tail=None

	def insert(self,val):
		if self.head==None:
			self.head=ListNode(val)
			self.tail=self.head
			return
		l=self.head
		while l.next!=None:
			l=l.next
		l.next=ListNode(val)
		self.tail=l.next
		return

	def length(self):
		if self.head==None:
			return 0
		c=1
		l=self.head
		while l.next!=None:
			c+=1
			l=l.next
		return c

	def rotate(self,k):
		if self.head==None:
			return
		t=self.head
		if k==0:
			return
		l=self.length()-k
		c=t
		while t.next!=None and l>0:
			l-=1
			c=t
			t=t.next

		self.tail.next=self.head
		c.next=None
		self.head=t

	def prin(self):
		t=self.head
		while t!=None:
			print(t.val,end=" ")
			t=t.next

g=R()
arr=list(map(int,input("Enter:").rstrip().split()))
for i in arr:
	g.insert(i)
b=int(input("shift:"))
l=g.length()
print(l)
b=b%l
print(b)
print("before:")
g.prin()
g.rotate(b)
print()
print("after:")
g.prin()
print()









