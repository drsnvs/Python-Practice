# 2. How will you remove last object from a list?

# pop() Function

# The simplest approach is to use the list's pop([i]) function, which removes an element present at the specified position in the list. If we don't specify any index, pop() removes and returns the last element in the list.

# Example:

list1 = [100,200,300,400,450]
print("Before Pop:",list1)
list1.pop()
print("After Pop:",list1)