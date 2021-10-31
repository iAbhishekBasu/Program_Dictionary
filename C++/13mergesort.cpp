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
void findmiddle(node*curr,node**first,node**second)
{
node*fast=curr->link;
node*slow=curr;
while(fast!=NULL&&fast->link!=NULL)
{
 
 slow=slow->link;
 fast=fast->link;

}

 *first=curr;
 *second=slow->link;
 slow->link=NULL;

}
node*mergeboth(node*first,node*second)
{
 node*answer=NULL;
 if(!first)
 {
  return second;
 }
 else if(!second)
 {
  return first;
 }
 if(first->data<=second->data)
 {
  answer=first;
  answer->link=mergeboth(first->link,second);

 }
 else
 {
  answer=second;
  answer->link=mergeboth(first,second->link);
 }
 return answer;
}
void mergesort(node**head)
{
 node*curr=*head;
 node*second;
 node*first;f
 if(!curr || !curr->link)
 return;
 
 findmiddle(curr,&first,&second);
 mergesort(&first);
 mergesort(&second);
 *head=mergeboth(first,second);
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
mergesort(&head);
display(head);
}