# 7. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

userInput = input("Enter String: ")
userInput = userInput.split()
list1 = []
for i in userInput:
    if len(i) >=2:
        if i[0] == i[len(i)-1]:
            list1.append(i)
print(len(list1),"String are Here: ")
print(list1)