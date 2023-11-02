#3.Write a Python program to calculate the area of regular polygon.
import math
#pi = 3.14 
n = float(input("Input number of sides: "))
N = float(input("Input the length of a side: "))
S = (n * N**2) / (4 * math.tan(math.pi/n))
print("The area of the polygon is: ", S )