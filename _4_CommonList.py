#Write a program to find out and display the common and the non-common
#elements in the list using membership operators.

list_1 = [1,2,3,4,5]
list_2 = [4,5,6,7,8]

if(list_1==list_2):
    print("Common List")
elif (list_1!=list_2):
    for i in list_1:
        for j in list_2:
            if i==j:
                k=i
                print(k,end=' ')
else:
    print("Not Common")
