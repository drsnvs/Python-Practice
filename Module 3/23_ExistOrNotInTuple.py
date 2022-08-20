# 23. Write a Python program to check whether an element exists within a tuple.

fruits = ("Mango","Apple","Orange","Banana")
check1 = "Mango"
check2 = "Poatato"

if check1 in fruits:
    print("Yes",check1,"in the Fruits")
else:
    print("No")

if check2 in fruits:
    print("Yes",check1,"in the Fruits")
else:
    print("No",check2,"is not in the Fruits")