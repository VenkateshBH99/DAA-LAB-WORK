#include <stdio.h>
#include <math.h>
void quickS(int a[],int l,int h){
	if(l<h){
		int pi=partition(a,l,h);
		quickS(a,l,pi-1);
		quickS(a,pi+1,h);
	}
	return;

}
int partition(int a[],int l,int h){
	int i=l-1;
	int r=a[h];
	for(int j=l;j<h+1;j++){
		if(a[j]<r){
			i=i+1;
			int t=a[j];
			a[j]=a[i];
			a[i]=t;
		}
	}
	int t=a[i+1];
		a[i+1]=a[h];
		a[h]=t;
	return i+1;
}
int main(){
	int n;
	printf("enter number of elements to be entered\n" );
	scanf("%d",&n);
	int a[n];
	for (int i = 0; i < n; ++i)
	{
		scanf("%d",&a[i]);

	}
	quickS(a,0,n-1);
	printf("sorted array is:\n" );
	for (int i = 0; i < n; ++i)
	{
		printf("%d\t",a[i]);
	}
	return 0;
	


}

