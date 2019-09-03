 def multilpy(A,B):
	n=len(A)
	R=[[None for j in range(n)] for i in range(n)]
	if n==1:
		R[0][0]=A[0][0]*B[0][0]
	else:
		L=int(n/2)
		a=[[None for j in range(L)] for i in range(L)]
		b=[[None for j in range(L)] for i in range(L)]
		c=[[None for j in range(L)] for i in range(L)]
		d=[[None for j in range(L)] for i in range(L)]
		e=[[None for j in range(L)] for i in range(L)]
		f=[[None for j in range(L)] for i in range(L)]
		g=[[None for j in range(L)] for i in range(L)]
		h=[[None for j in range(L)] for i in range(L)]
		
		a=spli(A,a,0,0)
		b=spli(A,b,0,L)
		c=spli(A,c,L,0)
		d=spli(A,d,L,L)

		e=spli(B,e,0,0)
		f=spli(B,f,0,L)
		g=spli(B,g,L,0)
		h=spli(B,h,L,L)

		P1=multilpy(a,sub(f,h))
		P2=multilpy(add(a,b),h)
		P3=multilpy(add(c,d),e)
		P4=multilpy(d,sub(g,e))
		P5=multilpy(add(a,d),add(e,h))
		P6=multilpy(sub(b,d),add(g,h))
		P7=multilpy(sub(a,c),add(e,f))

		c11=add(sub(add(P6,P5),P2),P4)
		c12=add(P1,P2)
		c21=add(P3,P4)
		C22=add(sub(P5,add(P3,P7)),P1)

		R=join(c11,R,0,0)
		R=join(c12,R,0,L)
		R=join(c21,R,L,0)
		R=join(C22,R,L,L)

	return R

def spli(A,a,i1,j1):
	u=int(i1)
	v=int(j1)
	for i in range(len(a)):
		v=j1
		for j in range(len(a)):
			a[i][j]=A[u][v]
			v+=1
		u+=1
	return a

def sub(W,Q):
	
	c=[[None for i in range(len(W))] for j in range(len(Q))]
	for i in range(len(Q)):
		for j in range(len(W)):
			c[i][j]=W[i][j]-Q[i][j]
	return c

def add(W,Q):
	c=[[None for i in range(len(W))] for j in range(len(Q))]
	for i in range(len(W)):
		for j in range(len(W)):
			c[i][j]=W[i][j]+Q[i][j]
	return c

def join(C,R,i1,j1):
	u=int(i1)
	v=int(j1)
	for i in range(len(C)):
		v=j1
		for j in range(len(C)):
			R[u][v]=C[i][j]
			v+=1
		u+=1
	return R

def main():
	f=open("text.txt","r")
	#n=int(input("Enter:"))
	n=int(f.readline())
	A=[[] for i in range(n)]
	B=[[] for i in range(n)]
	#print("Enter A:")
	for i in range(len(A)):
		A[i]=list(map(int,f.readline().rstrip().split()))
	print("Enter B:")
	for i in range(len(B)):
		B[i]=list(map(int,f.readline().rstrip().split()))
	print(A)
	print()
	print(B)
	R=multilpy(A,B)
	print("Result:")
	for i in R:
		for j in i:
			print(j,end=" ")
		print()
	f.close()
if __name__ == '__main__':
	main()

		



