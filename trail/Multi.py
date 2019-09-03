def makeEq(s1,s2):
	l1=len(s1)
	l2=len(s2)
	if l1>l2:
		for i in range(l1-l2):
			s2='0'+s2
		ar=[s1,s2,l1]
		return ar
	elif l2>l1:
		for i in range(l2>l1):
			s1='0'+s1
	ar=[s1,s2,l2]
	return ar

def add(s1,s2):
	ar=makeEq(s1,s2)
	s1=ar[0]
	s2=ar[1]
	l=ar[2]
	c=0
	r=''
	for i in range(l-1,-1,-1):
		a=int(s1[i])
		b=int(s2[i])
		su=(a^b^c)
		r=str(su)+r
		c=(a&b)|(b&c)|(c&a)
	if c:
		r='1'+r
	return r

def multiS(a,b):
	return int(a)*int(b)

def Mul(X,Y):
	ar=makeEq(X,Y)
	X=ar[0]
	Y=ar[1]
	l=ar[2]
	if l==0:
		return 0
	if l==1:
		return multiS(X,Y)

	fh=l//2
	sh=l-fh

	xl=X[:fh]
	xr=X[fh:]

	yl=Y[:fh]
	yr=Y[fh:]

	P1=Mul(xl,yl)
	P2=Mul(xr,yr)
	P3=Mul(add(xl,xr),add(yl,yr))

	return P1*(1<<(2*sh))+(P3-P2-P1)*(1<<(sh))+P2

e=input()
br=e.split(" ")
print(Mul(br[0],br[1]))
