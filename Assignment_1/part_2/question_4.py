import math
   #Taking input from the user for the first point (x1, x2)
x1=float (input ("Enter x-coordinate of the first point:"))
y1=float (input ("Enter y-coordinates of the first point"))
 #Taking input from the user for the second point (x2, y2)
x2=float (input ("Enter x-coordinates of the second point:"))
y2=float (input ("Enter y-coordinates of the second point:"))
distance=math.  sqrt ((x2-x1) ** 2+(y2-y1) ** 2)
print (f"The Euclidean distance between({x1}, {y1} and) and ({x2}, {y2}) is:{distance:.2f}")