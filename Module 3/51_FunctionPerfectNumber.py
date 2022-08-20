# 51. Write a Python function to check whether a number is perfect or not.

number = int(input("Enter Number For check Perfect or not : "))
def Perfection(number):
    sum = 0
    for i in range(1,number):
        if number%i==0:
            sum+=1
    if sum==0:
        print("Not Perfect.")
    else:
        print("Perfect.")
Perfection(number)