# 11. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
def square():
    list1 = []
    for i in range(1,31):
        list1.append(i*i)
    print("First Five :",list1[0:5])
    print("Last Five: ",list1[-1:-6:-1])

square()