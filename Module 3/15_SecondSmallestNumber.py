# 15. Write a Python program to find the second smallest number in a list.

def SecondSmallest(list1):
    list2 = []
    list1.sort()
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2[1]

list1 = [10,20,35,15,78,9,2,3,110,5,35,15,78,2,2]
print("Second Smallest Number is:",SecondSmallest(list1))