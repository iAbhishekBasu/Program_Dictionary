// C++ code to demonstrate star pattern
#include <iostream>
using namespace std;
 
// Function to demonstrate printing pattern
void pat(int n)
{
    // Outer loop to handle number of rows
    // n in this case
    int i = 0, j = 0;
    while (i < n) {
 
        // Inner loop to handle number of columns
        // values changing acc. to outer loop
        while (j <= i) {
 
            // Printing stars
            cout << "* ";
            j++;
        }
        j = 0; // we have to reset j value so as it can
               // start from beginning and print * equal to i.
        i++;
        // Ending line after each row
        cout << endl;
    }
}
 
// Driver Code
int main()
{
    int n = 5;
    pat(n);
    return 0;
}
/*
OUTPUT:
* 
* * 
* * * 
* * * * 
* * * * * 

*/
