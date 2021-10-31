import math 
import copy 

class Point(): 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  


def dist(p1, p2): 
    return math.sqrt((p1.x - p2.x) * 
                     (p1.x - p2.x) +
                     (p1.y - p2.y) * 
                     (p1.y - p2.y))  
  
def bruteForce(P, n): 
    min_val = float('inf')  
    for i in range(n): 
        for j in range(i + 1, n): 
            if dist(P[i], P[j]) < min_val: 
                min_val = dist(P[i], P[j]) 
                
  
    return min_val 
  

def stripClosest(strip, size, d): 
      
    min_val = d  
  
     
    for i in range(size): 
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val: 
            min_val = dist(strip[i], strip[j]) 
            j += 1
            if ans > min_val:
              X=strip[i]
              Y=strip[j]
              ans=min_val

  
    return min_val  
 
def closestUtil(P, Q, n): 
      
    # If there are 2 or 3 points, then use brute force  
    if n <= 3:  
        return bruteForce(P, n)  
    mid = n // 2
    midPoint = P[mid] 
   
    dl = closestUtil(P[:mid], Q, mid) 
    dr = closestUtil(P[mid:], Q, n - mid)  
    # Find the smaller of two distances  
    d = min(dl, dr) 
  
    strip = []  
    for i in range(n):  
        if abs(Q[i].x - midPoint.x) < d:  
            strip.append(Q[i]) 
  
    # Return the minimum of d and closest    
    ans =  min(d, stripClosest(strip, len(strip), d)) 
    return ans
  
 
def closest(P, n): 
    P.sort(key = lambda point: point.x) 
    Q = copy.deepcopy(P) 
    Q.sort(key = lambda point: point.y)     
  
    # Use recursive function closestUtil() to find the smallest distance  
    return closestUtil(P, Q, n) 


  
# Driver code 

n=int(input("Enter the total number of points in the 2D plane."))
P=[]
for i in range(0,n,1):
  x,y=[int(x) for x in input("Enter the coordinates for point %d = " %(i+1)).split()]    
  P.append(Point(x,y))
print("The smallest distance is", closest(P, n)) 
