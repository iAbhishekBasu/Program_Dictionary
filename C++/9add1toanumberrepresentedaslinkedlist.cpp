#include<bits/stdc++.h>
using namespace std;
struct node
{
 int data;
 node*link;
 node(int x)
 {
  data=x;
  link=NULL;
 }
};
node*push(node*head)
{
 int x;
 cin>>x;;
 node*temp=new node(x);
 if(head==NULL)
 {
  temp->link=NULL;
  return temp;
 }
 node*curr=head;
 while(curr->link!=NULL)
 {
  curr=curr->link;
 }
curr->link=temp;
temp->link=NULL;
return head;
}

void display(node*head)
{
 node*curr=head;
 while(curr!=NULL)
 {
  cout<<curr->data<<endl;
  curr=curr->link;

 }

}
node*reverse(node*head)
{
  node*curr=head;
  node*prev=NULL;
  node*next=NULL;
  while(curr!=NULL)
  {
    next=curr->link;

    curr->link=prev;
    prev=curr;
    curr=next;

  }
  return prev;
}
node*add1(node*head)
{
  node*curr=head;
  bool f=true;
  while(curr!=NULL&&f==true)
{
  if(curr->data==9 and curr->link==NULL)
  {
  curr->data=1;
  node*temp=new node(0);
  temp->link=head;
  head=temp;
  curr=curr->link;

  }
  else if(curr->data==9)
  {
    curr->data=0;
    curr=curr->link;
  }
  else
  {
    curr->data=curr->data+1;
    curr=curr->link;
    f=false;
  }

}
  return head;
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
head=reverse(head);
head=add1(head);
head=reverse(head);
display(head);
}