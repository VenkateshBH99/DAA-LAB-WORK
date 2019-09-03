def powe(x,n):
	if n==0:
		return 1
	temp=pow(x,n//2)
	if n%2==0:
		return temp*temp
	else:
		return x*temp*temp
x=int(input("Enter x:"))
n=int(input("Enter n:"))
print(powe(x,n))