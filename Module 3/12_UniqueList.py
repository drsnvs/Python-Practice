# 12. Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

list1 = [1,1,2,3,4,5,5,5,6,7,7,7,8]
print(unique(list1))