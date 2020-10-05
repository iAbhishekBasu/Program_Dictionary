#include<iostream>
int main() {
	int n,flag=0;
	std::cin>>n;
	for(int i=2;i<n;i++)
	{
if(n%i==0)
{
	std::cout<<"Not Prime";
	flag=-1;
	break;
}
}
if(flag==0)
{
	std::cout<<"Prime";
}
	return 0;
}
