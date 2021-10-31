#include <iostream>
using namespace std;

//Visualize it like a train ticket queue, passengers enter the line from the rear and exit from the front

int queue[100], n = 100, front = - 1, rear = - 1;  //initialize the queue size, rear and front as NA

//Insert element from the rear
void Insert() {
   int val;
   if (rear == n - 1)
   cout<<"Queue Overflow"<<endl;
   else {
      if (front == - 1)
      front = 0;
      cout<<"Insert the element in queue : "<<endl;
      cin>>val;
      rear++; 
      queue[rear] = val;
   }
}

//Delete element from the front
void Delete() {
   if (front == - 1 || front > rear) {
      cout<<"Queue Underflow ";
      return ;
   } else {
      cout<<"Element deleted from queue is : "<< queue[front] <<endl;
      front++;;
   }
}

//Display all the elements in the queue
void Display() {
   if (front == - 1)
   cout<<"Queue is empty"<<endl;
   else {
      cout<<"Queue elements are : ";
      for (int i = front; i <= rear; i++)
      cout<<queue[i]<<" ";
         cout<<endl;
   }
}
int main() {
   int ch;
   cout<<"1. Insert element to queue"<<endl;
   cout<<"2. Delete element from queue"<<endl;
   cout<<"3. Display all the elements of queue"<<endl;
   cout<<"4. Exit"<<endl;
   do {
      cout<<"Enter your choice : "<<endl;
      cin<<ch;
      switch (ch) {
         case 1: Insert();
         break;
         case 2: Delete();
         break;
         case 3: Display();
         break;
         case 4: cout<<"Exit"<<endl;
         break;
         default: cout<<"Please choose a valid option"<<endl;
      }
   } while(ch!=4);
   return 0;
}
