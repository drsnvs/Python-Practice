# 1. What is List? How will you reverse a list?

# reverse() Method:

# Every list in Python has a built-in reverse() method you can call to reverse the contents of the list object in-place. Reversing the list in-place means won't create a new list and copy the existing elements to it in reverse order.

# Example:

list1 = [10,20,30,40,50]

print("Before Reverse:",list1)
list1.reverse()
print("After Reverse:",list1)