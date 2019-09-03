import math as mt
v=8
e=11
T=[]
for i in range(v):
	if i is 0:
		temp=[0]*v
	else:
		temp=[mt.inf]*v
	T.append(temp)
G=[[0,1,10],[0,7,8],
    [1,5,2],
     [2,1,1],[2,3,1],
     [3,4,3],
     [4,5,-1],
     [5,2,-2],
     [6,5,-1],[6,1,-4],
     [7,6,1]]

M=[]
for i in range(v):
	temp=[mt.inf]*v
	M.append(temp)
#print(M,"  ",T)
for t in G:
	M[t[0]][t[1]]=t[2]
for k in range(1,v):
	for t in G:
		if T[t[1]][k]>T[t[0]][k-1]+M[t[0]][t[1]]:
			T[t[1]][k]=T[t[0]][k-1]+M[t[0]][t[1]]
#check for negative weight cycle
for t in G:
	
	if T[t[1]][k]>T[t[0]][k]+M[t[0]][t[1]]:
		print("Graph has a negative weight cycle")
		exit(1)
print(" ",end=" | ")

for i in range(v):
	print(i,end=" | ")
print()
for i in range(v):
	print("____",end="")
print()
for i in range(0,v):
	print(i,end=" | ")
	for j in range(v):
		if T[i][j] is mt.inf:
			print("-",end=" | ")
		else:
			print(T[i][j],end=" | ")
	print()




