# 8. Write a Python program to remove duplicates from a list.

def Duplicate(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

list1 = [10,20,30,40,50,10,20,30,40,50,60,70,80]

print(Duplicate(list1))