#Write a python program to find the sum of even numbers using command line
#arguments.

import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
a=0
b=0
c=0
if x%2==0:
    a=x
if y%2==0:
    b=y
if z%2==0:
    c=z
sum=a+b+c
print("The addition is :",sum)
