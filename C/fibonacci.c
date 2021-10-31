#include<stdio.h>
#include<conio.h>
int fibonacci(int);
int main(){ 
	int n, i; 
	printf("Enter the number of element you want in series :\n"); 
	scanf("%d",&n); 
	printf("fibonacci series is : \n");
	for(i=0;i<n;i++) { 
		printf("%d ",fibonacci(i));
	}
	getch();
}
 
int fibonacci(int n){ 
	if(n == 0)  //base condition 1
    return 0; 
	else if(n == 1) //base condition 2
    return 1; 
	else return (fibonacci(n-1) + fibonacci(n-2));  // recurrence relation
} 
