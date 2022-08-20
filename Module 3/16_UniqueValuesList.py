# 16. Write a Python program to get unique values from a list

def unique(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

list1 = [1,2,3,1,2,3,4,5,6,7]
print(unique(list1))