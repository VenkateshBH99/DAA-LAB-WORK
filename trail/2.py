def main():
	n=int(input("enter"))
	D=[0 for i in range(n+1)]
	for i in range(1,n+1):
		t=i
		while t<n+1:
			if D[t]==0:
				D[t]=1
			else:
				D[t]=0
			t=t+i

	for i in range(1,n+1):
		if D[i]==1:
			print(i,end=" ")

if __name__ == '__main__':
	main()