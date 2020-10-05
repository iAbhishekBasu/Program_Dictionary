#include<iostream>
using namespace std;
void fibSeries(int n)
{
	int a=1,b=1,c;
	for(int i=1;i<=n-2;i++)
	{
		c=a+b;
		a=b;
		b=c;
	}
	cout<<c;
	
  }

int main()
{
	int n;
	cin>>n;
	fibSeries(n);
	return 0;
}
