#include<stdio.h>

	int top=-1,stack[100],n=100;
	
void pop(){
	 
	 if(top==-1){
	 	printf("Stack is Empty.\n");
	 }
	 else{
	 	int y;
	 	y=stack[top];
	 	top--;
	 	printf("Popped %d \n",y);
	 }
	 
}

  void push(){
  	     
  	     if(top==n-1){
  	     	printf("Stack is Full \n ");
		   }
		   else{
		   	int y;
		   	 top++;
		   	 printf("Enter the number to be pushed \n");
		   	 scanf("%d",&y);
		   	 stack[top]=y;
		   	 printf("Pushed\n");
		   }
  }
  void display(){
  	
  	    if(top==-1){
  	    	printf("Stack is empty \n");
		  }
		  else{
		  	
		  	printf("Elements In Stack: \n");
		  	for(int i=0;i<=top;i++){
		  		printf("%d ",stack[i]);
			  } 
			  
			  printf("\n");
		  }
  }
int main(){
          int x;
          
          while(1){
          	
          	printf("Choose:1 for Pop: \n");
          	printf("Choose:2 for Push: \n");
          	printf("Choose:3 for Display: \n");
          	 scanf("%d",&x);
		  
          switch(x){
          	
          	case 1: pop();
          	        break;
          	        
         case 2: push();
                 break;
                 
         case 3: display();
		          break;
				  
	      default : 
		    printf("Invalid Input \n");        
		  }
}
}
