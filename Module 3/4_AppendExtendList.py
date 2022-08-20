# 4. Differentiate between append () and extend () methods?

# append() adds a single element to the end of the list while . extend() can add multiple individual elements to the end of the list.

# Example:

list1 = [10,20,30,40,50]

# Let's Append a one element in list1.
list1.append(60)
print("After Append :",list1)

# extend takes iterable items.
list1.extend([70,80,90,100])
print("After Extend :",list1)