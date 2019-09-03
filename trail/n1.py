class pair1:
	def __init__(self,n):
		self.gender=[[] for i in range(n)]

	def addGender(self,i,j):
		self.gender[i-1].append(j-1)

class visit:
	def __init__(self,k,index):
		self.g=k
		self.v="free"
		self.match=None
		self.d=0
		self.ind=[None for i in range(len(index))]
		for i in range(len(index)):
			self.ind[index[i]]=i
		

def Match(male,female):
	M=[visit(k,male[k]) for k in range(len(male))]
	F=[visit(k,female[k]) for k in range(len(female))]
	j=0
	q=[]
	
	for i in M:
		q.append(i)
	while q:
		m=q.pop(0)
		while m.d!=len(male[m.g]) and m.v=="free":
			if F[male[m.g][m.d]].v=="free":
				F[male[m.g][m.d]].match=m.g
				F[male[m.g][m.d]].v="paired"
				m.v="paired"
				m.match=male[m.g][m.d]
				m.d+=1
			else:
				#a=female[m.d].index(m.g)
				#b=female[m.d].index(F[m.d].match)
				a=F[male[m.g][m.d]].ind[m.g]
				b=F[male[m.g][m.d]].ind[F[male[m.g][m.d]].match]
				if a<b:
					M[F[male[m.g][m.d]].match].v="free"
					q.append(M[F[male[m.g][m.d]].match])
					F[male[m.g][m.d]].match=m.g
					m.v="paired"
					m.match=male[m.g][m.d]
					m.d+=1
				else:
					m.d+=1
					
	r=[]
	r.append(male)
	r.append(M)
	r.append(female)
	r.append(F)
	return r

def main():
	m1=int(input("Enter number of male:"))
	f1=int(input("Enter number of females"))
	M1=pair1(m1)
	F1=pair1(f1)
	for i in range(m1):
		print("Enter preference of :",(i+1)," male. Given ",f1," females: ",end="")
		n=input()
		ar=list(map(int,n.rstrip().split()))
		for j in ar:
			M1.addGender(i+1,j)
	for i in range(f1):
		print("Enter preference of :",(i+1)," female. Given ",m1," males: ")
		n=input()
		ar=list(map(int,n.rstrip().split()))
		for j in ar:
			F1.addGender(i+1,j)
	res=Match(M1.gender,F1.gender)
	print("matches:")
	print("male     females")
	for i in range(len(res[1])):

		if res[1][i].match!=None:
			print((i+1),"  -  ",(res[1][i].match+1))
		else:
			print((i+1),"  -   None")






if __name__ == '__main__':
	main()


	
