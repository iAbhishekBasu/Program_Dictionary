#include<bits/stdc++.h>
using namespace std;
struct node
{
 int data;
 node*link;
 node*plink;
 node(int x)
 {
  data=x;
  link=NULL;
  plink=NULL;
 }
};
node*push(node*head)
{
 int x;
 cin>>x;
 node*temp=new node(x);
 if(head==NULL)
 {
  return temp;
 }
 node*curr=head;
 while(curr->link!=NULL)
 {
  curr=curr->link;
 }
 curr->link=temp;
 temp->plink=curr;
 return head;
}
void display(node*head)
{
 node*curr=head;
 while(curr!=NULL)
 {
  cout<<curr->data<<" ";
  curr=curr->link;
 }
 cout<<endl;
}
void pairsum(node*head)
{
 int x;
 cin>>x;
 node*first=head;
 node*second=head;
 while(second->link!=NULL)
 {
  second=second->link;
 }
 bool found=false;
 while(first!=NULL&&second!=NULL&&first!=second&&second->link!=first)
 {
  if((first->data+second->data)==x)
  {
   found=true;
    cout<<first->data<<" "<<second->data<<" "<<endl;
  first=first->link;
  second=second->plink;
  }
  else{
   if((first->data+second->data)<x)
   {
    first=first->link;
   }
   else
   second=second->plink;
  }
 }
 if(found==false)
 {
  cout<<"no pair found"<<endl;
 }
}
int main()
{
 node*head=NULL;
 int x;
 cin>>x;
 for(int i=0;i<x;i++)
 {
  head=push(head);
 }
 pairsum(head);

}