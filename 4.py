# A Program to find the area of the circle which takes radius input from user and calculates its area
from math import pi
r=float(input("Enter radius of circle: "))
area= pi * (r**2)
print("Area of the circle of radius ",r," is ",round(area,2)) 
