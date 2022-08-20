# 33. Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'c': 3,
           'a': 1,
           'd': 4,
           'b': 2}
 
# Sorting dictionary
# sorted_dict = sorted([(value, key) for (key, value) in my_dict.items()])
 
# # Print sorted dictionary
# print("Sorted dictionary is :")
# print(sorted_dict)

# sorted = sorted(my_dict.items())
# print(sorted)

for i,j in sorted(my_dict.items()):
    print(i,":",j)

unsort = sorted(my_dict.items())

for i in range(len(unsort)-1,-1,-1):
    print(unsort[i])