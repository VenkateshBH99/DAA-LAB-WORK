def mul(A,B):
	n=len(A)
	R=[]
	if n==1:
		for i in B:
			R.append(A[0]*i)
	else:
		L=n//2
		a0=A[:L]
		a1=A[L:]
		b0=B[:L]
		b1=B[L:]
		P1=mul(a0,b0)
		P2=mul(add(a0,a1),add(b0,b1))
		P3=mul(a1,b1)
		Y=sub(sub(P2,P1),P3)
		R=app(app(P1,Y,L),P3,L+L)
	return R
def add(A,B):
	c=[]
	i=0
	while i<len(A) and i<len(B):
		c.append(A[i]+B[i])
		i+=1
	while i<len(A):
		c.append(A[i])
		i+=1
	while i<len(B):
		c.append(B[i])
		i+=1
	return c
def sub(A,B):
	c=[]
	i=0
	while i<len(A) and i<len(B):
		c.append(A[i]-B[i])
		i+=1
	while i<len(A):
		c.append(A[i])
		i+=1
	while i<len(B):
		c.append(B[i])
		i+=1
	return c
def app(A,B,r):
	c=[]
	i=0
	j=0
	while j<len(B):
		if i<len(A):
			if i==r:
				c.append(A[i]+B[j])
				j+=1
				r+=1
			else:
				c.append(A[i])
			i+=1
		else:
			c.append(B[j])
			j+=1
	return c

B=[1,2,3]
A=[1,1,1,1]
if len(A)>len(B):
	A,B=B,A
print(mul(A,B))

