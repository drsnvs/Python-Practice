#Write a program to search an element in the list using for loop and also
#demonstrate the use of “else” with for loop.

list_1 = [10,20,30,40,50,60,70,80,90,100]
user = int(input("Enter Number Found in list :"))
for i in list_1:
    if i == user:
        print("It is in the list",i)
        
else:
    print("For Loop Done")
