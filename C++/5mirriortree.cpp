#include<bits/stdc++.h>
using namespace std;
struct node
{
 int data;
 node*left;
 node*right;
 node(int x)
 {
  data=x;
  left=NULL;
  right=NULL;
 }
};
node*inserte(node*root)
{
 int x;
 cin>>x;
 node*temp=new node(x);
  if(root==NULL)
  {
   return temp;
  }
  queue<node*>q;
  q.push(root);
  while(!q.empty())
  {
   node*curr=q.front();
   q.pop();
   if(curr->left!=NULL)
   {
    q.push(curr->left);
   
   }
   else
   {
    curr->left=temp;
    return root;
   }
   if(curr->right!=NULL)
   {
    q.push(curr->right);
   }
   else
   {
    curr->right=temp;
    return root;
   }

  }
  return root;
}
void levelorderdisplay(node*root)
{
 if(!root)
 {
  return;
 }
 queue<node*>q;
 q.push(root);
 while(!q.empty())
 {
  node*curr=q.front();
  cout<<curr->data<<endl;
  if(curr->left)
  q.push(curr->left);
  if(curr->right)
  {
   q.push(curr->right);
  }
  q.pop();
 }
}
int countlevel(node*root)
{
 if(!root)
 return 0;
 int x=countlevel(root->left);
 int y=countlevel(root->right);
 return (max(x,y)+1);
}
void mirrior(node*root)
{
 if(!root)
 return ;
 mirrior(root->left);
 mirrior(root->right);
 swap(root->left,root->right);
}
int main()
{
 node*root=NULL;
int x;
cin>>x;
for(int i=0;i<x;i++)
{
 root=inserte(root);
}
mirrior(root);
levelorderdisplay(root);
}
void makemirror(TreeNode*root)
    {
        if(root==NULL)
            return;
        makemirror(root->left);
        makemirror(root->right);
        swap(root->left,root->right);
    }

bool checksame(TreeNode*p,TreeNode*t)
    {
        if(p==NULL&&t==NULL)
           return true;
        if(p==NULL||t==NULL)
            return false;
        
       else 
        {
           bool c=p->val==t->val;
           bool e=checksame(p->left,t->left);
           bool d=checksame(p->right,t->right);
           cout<<c<<" "<<e<<" "<<d<<endl;
           if(c&&d&&e)
           return true;
        else
            return false;
        }
  
    }
    void display(TreeNode*p)
    {
        if(p!=NULL)
        {
        cout<<p->val<<" ";
        display(p->left);
        display(p->right);
        }
        else
        {
            cout<<"null"<<" ";
        }
    }
    bool isSymmetric(TreeNode* root) {
       TreeNode*p=root;
        makemirror(p);

      return checksame(p,root);
    }










    TreeNode* rleft = root->left;
        TreeNode* rright = root->right;
        return checksame(rleft,rright);





        if(p==NULL && q==NULL )
            return true;
        if(p==NULL || q==NULL)
            return false;
        else{
            bool c1 = p->val==q->val;
            bool c2 = checksame(p->left,q->right);
            bool c3 = checksame(p->right,q->left);
            if(c1 && c2 && c3)return true;
            return false;
        }