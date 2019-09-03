helper=[[None for j in range(4)] for i in range(4)]
def get_path(i,j):
	if helper[i][j]==None:
		print(i," ",j)
		return
	get_path(i,helper[i][j])
	get_path(helper[i][j],j)


def main():
	inf=float("infinity")
	A=[[0,float("infinity"),3,float("infinity")],[2,0,float("infinity"),float("infinity")],[float("infinity"),7,0,1],[6,float("infinity"),float("infinity"),0]]
	
	for i in range(len(A)):
		for j in range(len(A)):
			if A[i][j]!=float("infinity"):
				helper[i][j]=None
	for i in A:
		for j in i:
			print(j,end=" ")
		print()
	print(A[0][0])
	for k in range(len(A)):
		for i in range(len(A)):
			for j in range(len(A[0])):
				if A[i][j]>A[i][k]+A[k][j]:
					A[i][j]=A[i][k]+A[k][j]
					helper[i][j]=k

	for i in A:
		for j in i:
			print(j,end=" ")
		print()

	get_path(3,1)


if __name__ == '__main__':
	main()