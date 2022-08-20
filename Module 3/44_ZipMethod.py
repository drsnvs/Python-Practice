# 44. Why Do You Use the Zip () Method in Python?

name = ['darshan','ritik','karan','ronit']
roll_num = [1,2,3,4]
zippList = list(zip(name,roll_num))
zippTuple = tuple(zip(name,roll_num))
zippDict = dict(zip(name,roll_num))

print(zippList)
print(zippTuple)
print(zippDict)