# 32. How will you create a dictionary using tuples in python?

tuple1 = (("Name","Darshan"),("Age",18),("City","Ahmedabad"))
dict1 = dict((x,y) for x,y in tuple1)
print(dict1)