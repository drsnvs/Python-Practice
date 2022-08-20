# 38. Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

class10 = {}
def createStudent(num):
    for i in range(1,num+1):
        class10.setdefault(i,f'Student {i}')

createStudent(35)
for i in class10:
    if i<=15:
        print(i,':',class10[i])