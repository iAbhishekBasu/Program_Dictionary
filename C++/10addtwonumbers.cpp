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
node*add(node*head1,node*head2)
{
 head1=reverse(head1);
 head2=reverse(head2);
 int c=0;
 int s=0;
 node*temp;
 node*res=NULL;
 node*cur=NULL;
 while(head1!=NULL||head2!=NULL)
 {
    s=c+(head1?head1->data:0)+(head2?head2->data:0);
    c=(s>=10)?1:0;
    s=s%10;
    temp=new node(s);
    if(res==NULL)res=temp;
    else
    cur->link=temp;
    
    cur=temp;
    if(head1)
    head1=head1->link;
    if(head2)
    {
    head2=head2->link;
    }
    
    
 }
 if(c>0)
 {
  temp=new node(c);
  cur->link=temp;
  cur=temp;
 }

 return res;
}
int main()
{
node*head1=NULL;
node*head2=NULL;
int x;
cin>>x;
for(int i=0;i<x;i++)
{
 head1=push(head1);
}
int y;
cin>>y;
for(int i=0;i<y;i++)
{
 head2=push(head2);
}

node*head=add(head1,head2);
head=reverse(head);
display(head);
}