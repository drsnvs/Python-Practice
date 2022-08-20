# 6. How will you compare two lists?

list1 = [10,20,30,40,50,60,70,80]
list2 = [60,70,80,90,100,110,120]

list3 = []
list4 = []
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
        
print("Same Elements are:",list3)