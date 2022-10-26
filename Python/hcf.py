# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# Identify the Numbers' Precedence
    small, big = y, x if x > y else x, y
    for i in range(small, big+1, small):
        if big % i == 0:
            return i
    return 1

if __name__ == "__main__":
    num1 = 54 
    num2 = 24
    print("The H.C.F. is", compute_hcf(num1, num2))
