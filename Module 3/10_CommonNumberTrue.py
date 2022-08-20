# 10. Write a Python function that takes two lists and returns true if they have at least one common member.

def common(list1,list2):
    list3 = []
    for i in list1:
        for j in list2:
            if i==j:
                list3.append(i)
    return list3

list1 = [1,2,3,4,5,7,6]
list2 = [8,9,10,11,1,2,3]
print(common(list1,list2))