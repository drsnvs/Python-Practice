# 31. Write a Python program to convert a list of tuples into a dictionary.

tuple1 = ("Name","Age","Address","City")
dict1 = dict()
dict1 = dict1.fromkeys(tuple1)
print(dict1)