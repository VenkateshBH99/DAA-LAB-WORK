import math
class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
def compareX(A,B):
	if A.x<B.y:
		return True
	return False

def compareY(A,B):
	if A.y<B.y:
		return True
	return False
def qsort(arr,r):
	if len(arr)>1:
		mid=len(arr)//2
		L=arr[:mid]
		R=arr[mid:]
		qsort(L,r)
		qsort(R,r)
		i=j=k=0
		while i<len(L) and j<len(R):
			if r=="x":
				if compareX(L[i],R[j]):
					arr[k]=L[i]
					i+=1
				else:
					arr[k]=R[j]
					j+=1
				k+=1
			else:
				if compareY(L[i],R[j]):
					arr[k]=L[i]
					i+=1
				else:
					arr[k]=R[j]
					j+=1
				k+=1

		while i<len(L):
			arr[k]=L[i]
			i+=1
			k+=1
		while j<len(R):
			arr[k]=R[j]
			j+=1
			k+=1
	return

def dist(p1,p2):
	return math.sqrt(pow((p1.x-p2.x),2)+pow((p1.y-p2.y),2))

def bruteForce(P,n):
	min=float("infinity")
	for i in range(n):
		for j in range(i+1,n):
			if dist(P[i],P[j])<min:
				min=dist(P[i],P[j])
	return min

def stripClosest(strip,size,d):
	mi=d
	for i in range(len(strip)):
		j=i+1
		while j<len(strip) and (strip[j].y-strip[i].y)<mi:
			if dist(strip[i],strip[j])<mi:
				mi=dist(strip[i],strip[j])
	return mi

def closestUtil(Px,Py,n):
	if n<=3:
		return bruteForce(P,n)
	mid=n//2
	midPoint=P[mid]
	Pyl=[]
	Pyr=[]
	for i in range(n):
		if Py[i].x<=midPoint.x:
			Pyl.append(Py[i])
		else:
			Pyr.append(Py[i])

	L=P[:mid]
	R=P[mid:]
	dl=closestUtil(L,Pyl,len(L))
	dr=closestUtil(R,Pyr,len(R))

	d=min(dl,dr)
	strip=[]
	for i in range(n):
		if abs(Py[i].x-midPoint.x)<d:
			strip.append(Py[i])

	return min(d,stripClosest(strip,len(strip),d))


def closest(P,n):
	Px=[]
	Py=[]
	for i in P:
		Px.append(i)
		Py.append(i)
	qsort(Px,"x")
	qsort(Py,"y")
	return closestUtil(Px,Py,n)



n=int(input("Enter number of points to be entered:"))
print("Enter :")
P=[]
for i in range(n):
	e=list(map(int,input().rstrip().split()))
	P.append(point(e[0],e[1]))
print("Ok")
print("The smallest distance is:",closest(P,len(P)))
