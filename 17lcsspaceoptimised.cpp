#include<bits/stdc++.h>
using namespace std;
int main()
{
string s;
string p;
cin>>s;
cin>>p;
int x=s.size();
int y=p.size();
int dp[2][y+1];
for(int i=0;i<2;i++)
{
 for(int j=0;j<=y;j++)
 {
  dp[i][j]=0;
 }
}
for(int i=0;i<=x;i++)
{
 for(int j=0;j<=y;j++)
 {
  if(i==0||j==0)
  {
   dp[i%2][j]=0;
  }
  else if(s[i-1]==p[j-1])
  {
    dp[i%2][j]=1+dp[(i+1)%2][j-1];
  }
  else
  {
   dp[i%2][j]=max(dp[i%2][j-1],dp[(i+1)%2][j]);
  }
 }
 
}
cout<<dp[x%2][y]<<endl;
}