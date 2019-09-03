def main():
	inf=float("infinity")
	A=[[0,float("infinity"),3,float("infinity")],[2,0,float("infinity"),float("infinity")],[float("infinity"),7,0,1],[6,float("infinity"),float("infinity"),0]]
	for i in A:
		for j in i:
			print(j,end=" ")
		print()
	print(A[0][0])
	for k in range(len(A)):
		for i in range(len(A)):
			for j in range(len(A[0])):

				A[i][j]=min(A[i][j],A[i][k]+A[k][j])

	for i in A:
		for j in i:
			print(j,end=" ")
		print()
if __name__ == '__main__':
	main()