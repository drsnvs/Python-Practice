#Write a menu driven python program which perform the following:
#• Find area of circle
#• Find area of triangle
#• Find area of square and rectangle
#• Find Simple Interest

PI = 3.141593
r = int(input("Enter r : "))
circle = (2*PI*(r*r))
print("Circle:",circle)

base = int(input("Enter base : "))
height = int(input("Enter height : "))
triangle = 0.5*base*height
print("Triangle:",triangle)

length = int(input("Enter length : "))
width = int(input("Enter width : "))
rectangle = length*width
print("Rectangle:",rectangle)

square = length*length
print("Square:",square)

p = int(input("Enter principle : "))
ra = int(input("Enter rate : "))
n = int(input("Enter time : "))
si = (p*r*n)/100

print("Simple Interest:",si)
