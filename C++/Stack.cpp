#include <iostream>
using namespace std;

int stack[100], n=100, top=-1; //initialize the stack length, and top as -1 for empty stack

//Function to add value to the stack
void push(int val) {
   if(top >= n-1)  //case when the stack is full
   cout<<"Stack Overflow"<<endl;
   else {
      top++; // otherwise increment the top index value and add an element to the stack
      stack[top]=val;
   }
}

//Function to remove value from the stack
void pop() {
   if(top <= -1)
    cout<<"Stack Underflow"<<endl;
   else {
      cout<<"The popped element is:"<< stack[top] <<endl;
      top--;  //decrement the top counter
   }
}

//Function to display all the elements in the stack starting from index 0
void display() {
   if(top >= 0) {    //If the stack is not empty
      cout<<"Stack elements are:";
      for(int i=top; i>=0; i--)
        cout<<stack[i]<<" ";
      cout<<endl;
   } else
   cout<<"Stack is empty";
}
int main() {
   int ch, val;
   cout<<"1. Push in stack"<<endl;
   cout<<"2. Pop from stack"<<endl;
   cout<<"3. Display stack"<<endl;
   cout<<"4. Exit"<<endl;
   do {
      cout<<"Enter choice: "<<endl;
      cin>>ch;
      switch(ch) {
         case 1: {
            cout<<"Enter value to enter in the stack:"<<endl;
            cin>>val;
            push(val);
            break;
         }
         case 2: {
            pop();
            break;
         }
         case 3: {
            display();
            break;
         }
         case 4: {
            cout<<"Exit"<<endl;
            break;
         }
         default: {
            cout<<"Please select a valid option as shown in the menu"<<endl;
         }
      }
   }while(ch!=4);
   return 0;
}
