# 49. Write a Python function to calculate the factorial of a number (a non-negative integer)


def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact = fact * i
        print(fact)
input_Fact = int(input("Enter Number For Factorial: "))
if input_Fact>=0:
    factorial(input_Fact)
else:
    print("Enter Positive Number")