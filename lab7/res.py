class Res:
	def __init__(self):
		self.brr=[]
		self.fin=0
n=int(input("Enter the number of intervals:"))
arr=[]
for i in range(n):
	arr.append(list(map(int,input().rstrip().split())))
arr.sort(key=lambda k:k[0])
r=[]
for i in range(len(arr)):
	t=0
	for j in r:
		if j.fin<=arr[i][0]:
			t=1
			j.brr.append(arr[i])
			j.fin=arr[i][1]
			break
	if t==0:
		g=Res()
		g.brr.append(arr[i])
		g.fin=arr[i][1]
		r.append(g)	
print("Minimum number of resources:",len(r))
for i in range(len(r)):
	print("Resourse",i+1,"jobs:",r[i].brr)




		


