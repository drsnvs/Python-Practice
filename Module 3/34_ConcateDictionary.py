# 34. Write a Python script to concatenate following dictionaries to create a new one

from operator import concat
from turtle import update


dict1 = {
    'a':1,
    'b':2,
    'c':3,
}
dict2 = {
    'x':10,
    'y':20,
    'z':30,
}

dict3 = {}
for i in (dict1,dict2):
    dict3.update(i)

print(dict3)