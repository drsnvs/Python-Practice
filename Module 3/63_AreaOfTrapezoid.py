# 63. Write a Python program to calculate the area of a trapezoid

# trapezoid = ½ (a + b) h

def trapezoid(base1,base2,height):
    return (base1+base2) * height/2

print(trapezoid(10,20,3))