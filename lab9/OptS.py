x=input("Enter 1 String:")
y=input("Enter 2 String:")
T=[[None for j in range(len(y)+1)] for i in range(len(x)+1)]

T1=[[None for j in range(len(y)+1)] for i in range(len(x)+1)]

for k in range(len(T)):
	T[k][0]=k
	T1[k][0]=k
for k in range(len(T[0])):
	T[0][k]=k
	T1[0][k]=k
class link:
	def __init__(self):
		self.L=[[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]

	def addL(self,i,j,a,b):
		self.L[a][b]=(i,j)

l=link()
def minimum(i,j,a1,S1,a2,S2,a3,S3):
	r=[]
	mi=min(S1[2],S2[2],S3[2])
	if mi==S1[2]:
		r=[S1[0],S1[1],a1+S1[2]]
	elif mi==S2[2]:
		r=[S2[0],S2[1],a2+S2[2]]
	else:
		r=[S3[0],S3[1],a3+S3[2]]
	return r
def E(i,j):
	if T[i][j]!=None:
		return [i,j,T[i][j]]
	mi=minimum(i,j,diff(i,j),E(i-1,j-1),1,E(i-1,j),1,E(i,j-1))
	
	T[i][j]=mi[2]
	l.addL(mi[0],mi[1],i,j)
	return [i,j,T[i][j]]

def diff(i,j):
	if x[i-1]==y[j-1]:
		return 0
	return 1

def E1():
	for j in range(1,len(T1[0])):
		for i in range(1,len(T1)):
			T1[i][j]=min(diff(i,j)+T1[i-1][j-1],1+T1[i-1][j],1+T1[i][j-1])
	return T1[len(x)][len(y)]

def prin(g,t2):
	g1=l.L[g[0]][g[1]]
	if g[0]!=-1 and g[1]!=-1:
		if g1[0]==g[0]:
			print("_",end=" ")
		else:
			print(x[g[0]-1],end=" ")
		if g1[1]==g[1]:
			print("_",end=" ")
		else:
			print(y[g[1]-1],end=" ")
		print(diff(g[0],g[1]))
	


res=E(len(x),len(y))
t=[res[0],res[1]]
t2=t
prin(t,t2)

while l.L[t[0]][t[1]]!=-1 and (t[0]!=0 and t[1]!=0):
	g=l.L[t[0]][t[1]]
	prin(g,t2)
	#break
	t2=t
	t=[g[0],g[1]]




print(res[2])
print(E1())
