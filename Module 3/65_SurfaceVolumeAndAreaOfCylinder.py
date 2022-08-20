# 65. Write a Python program to calculate surface volume and area of a cylinder

# A cylinder's volume is π r² h, and its surface area is 2π r h + 2π r².

def cylinderVolume(r,h):
    return ((22/7)*(r*r)*h)

def surfaceArea(r,h):
    return ( (2*(22/7))*r*h ) + ( (2*(22/7))*r*r )

print(cylinderVolume(6,4))
print(surfaceArea(6,4))