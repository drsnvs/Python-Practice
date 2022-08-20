# 27. Write a Python program to replace last value of tuples in a list.

# We cannot change tuple's  elements
Languages = ("Python","Java","Php","C++","C")
Languages = list(Languages)
Languages[-1] = Languages[-1].replace("C","Advance C",1)
Languages = tuple(Languages)
print(Languages)