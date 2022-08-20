# 17. Write a Python program to check whether a list contains a sub list

list1 = [10,20,30,40,50,60,70]
subList = [10,20,30]
ans = False
for i in subList:
    if i in list1:
        ans = True
print(ans)