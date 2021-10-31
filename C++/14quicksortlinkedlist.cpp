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
node*partition(node*head,node*end,node**newhead,node**newend)
{
 node*pivot=end;
 node*prev=NULL;
 node*curr=head;
 node*tail=pivot;
 while(curr!=pivot)
 {
  if(curr->data<pivot->data)
  {
   if((*newhead)==NULL)
      *newhead=curr;
   prev=curr;
   curr=curr->link;
  }
  else
  {
   if(prev)
   {
    prev->link=curr->link;
    

   }
   node*temp=curr->link;
   curr->link=NULL;
   tail->link=curr;
   tail=curr;
   curr=temp;
  }
 }
 if((*newhead)==NULL)
 (*newhead)=pivot;
 (*newend)=tail;
 return pivot;
}
node*quicksort(node*head,node*ende)
{
 
 if(!head||head==ende)
 {
   return head;
 }
 node*newhead=NULL;
 node*newend=NULL;
 node*pivot=partition(head,ende,&newhead,&newend);
 if(newhead!=pivot)
 {
  node*temp=newhead;
  while(temp->link!=pivot)
  {
   temp=temp->link;
  }
  temp->link=NULL;
  newhead=quicksort(newhead,temp);
  
  while(temp->link!=NULL)
  {
   temp=temp->link;
  }
   temp->link=pivot;
 }
 pivot->link=quicksort(pivot->link,newend);
 return newhead;
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
node*end=head;
while(end->link!=NULL)
{
 end=end->link;
}
head=quicksort(head,end);
display(head);
}