import heapq as heapq
import collections

G=[]
class Node:
	def __init__(self,freq,sym):
		self.freq=freq
		self.sym=sym
		self.left=None
		self.right=None

	def __lt__(self,other):
		return self.freq<other.freq

def printCode(root,s):
	if root.left==None and root.right==None:
		print(root.sym,":",s)
		G.append([root.sym,s,root.freq])
		return
	printCode(root.left,s+"0")
	printCode(root.right,s+"1")
	

def Huffman(F):
	
	h=[]
	for i in range(len(F)):
		node=Node(F[i][1],F[i][0])
		heapq.heappush(h,(F[i][1],node))
	for i in range(len(F)-1):
		t1=heapq.heappop(h)
		t2=heapq.heappop(h)
		node=Node(t1[1].freq+t2[1].freq,None)
		node.right=t1[1]
		node.left=t2[1]
		heapq.heappush(h,(node.freq,node))
	return heapq.heappop(h)


ch=int(input("1.String\n2.freq and symb\n3.File\nEnter your choice:"))
if ch==1:
	st=input("Enter:")
	d=collections.defaultdict(int)
	for c in st:
		d[c]+=1
	F=[]
	for c in d:
		F.append([c,d[c]])
	
	res=Huffman(F)
	printCode(res[1],"")
elif ch==2:
	n=int(input("Enter number of node:"))
	F=[]
	for i in range(n):
		a=list(map(str,input().rstrip().split()))
		F.append([a[0],int(a[1])])
	res=Huffman(F)
	printCode(res[1],"")
else:
	name=input("Enter file name:")
	fname=open(name,'r')
	st=fname.readline()
	d=collections.defaultdict(int)
	while st:
		for c in st:
			d[c]+=1
		st=fname.readline()

	fname.close()
	F=[]
	for c in d:
		F.append([c,d[c]])
	print(F)
	res=Huffman(F)
	printCode(res[1],"")
	f1=open("encoded.txt",'w')
	fname=open(name,'r')
	st=fname.readline()
	while st:
		for c in st:
			for c1 in G:
				if c1[0]==c:
					f1.write(c1[1])
		st=fname.readline()
	fname.close()
	f1.close()

print("Size of the Encoded file:",end="")
sum=0
for i in G:
	sum+=len(i[1])*i[2]
print(sum)

if ch==3:
	ch1=input("Want to decode the file?Y/N:")
	if ch1=="y" or ch=="Y":
		f1=open("encoded.txt",'r')
		st=f1.readline()
		su=""
		for c in st:
			su+=c
			for c1 in G:
				if c1[1]==su:
					print(c1[0],end="")
					su=""
		print()
		#print(st)
		f1.close()








	
