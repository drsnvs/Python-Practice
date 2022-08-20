# 5. Write a Python function to get the largest number, smallest num and sum of all from a list.

def LargeSmallSum(*num):
    print("You Entered:",num)
    sum = 0
    for i in num:
        sum = i + sum
    print("Sum is:",sum)
    num = list(num)
    lenn = len(num)
    num.sort()
    print("Largest Number is:",num[lenn-1])
    print("Smallest Number is:",num[0])
print("\nFirst Example:")
LargeSmallSum(15,8,60,79,25,15)
print("\nSecond Example:")
LargeSmallSum(10,50,70,20,30,40,50,70,100)