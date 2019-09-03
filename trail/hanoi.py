def solveHanoi(n,f,i,t):
	if n==1:
		print("move 1 from ",f," to ",t)
		return
	solveHanoi(n-1,f,t,i)
	print("move",n,"from ",f," to ",t)
	solveHanoi(n-1,i,f,t)


n=int(input())
solveHanoi(n,"A","B","C") 