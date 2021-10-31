import random

def printParenthesis(m, j, i ):
  if j == i:
    # The first matrix is printed as 'A', next as 'B' etc
    print(chr(65 + j), end = "")
    return
  else:
    print("(", end = "")
    printParenthesis(m, m[j][i] - 1, i)
    printParenthesis(m, j, m[j][i])
    print (")", end = "" )

def matrixChainOrder(p, n):
    m = [[0 for i in range(n)]for i in range (n)]
 
    for l in range (2, n + 1):
        for i in range (n - l + 1):
            j = i + l - 1
            m[i][j] = float('Inf')
            for k in range (i, j):
                current_cost = (m[i][k] + m[k + 1][j] + (p[i] * p[k + 1] * p[j + 1]));
                if (current_cost < m[i][j]):
                    m[i][j] = current_cost
                    # Storing k value in opposite index.
                    m[j][i] = k + 1
    return m;

#main
size = int (input("enter the length of the matrix chain: ")) 
arr = []
for i in range(size):
  a = random.randint(1,9)
  arr.append(a)
print(arr)
n=size-1
m = matrixChainOrder(arr, n)
print("Optimal Parenthesization is: ", end = "")
printParenthesis(m, n - 1, 0)
print("\nOptimal Cost is :", m[0][n - 1])
