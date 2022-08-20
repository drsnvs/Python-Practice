# 28. Write a Python program to find the repeated items of a tuple.

Degree = ("bcom","bba","bca","bed","btech","bcom","bba")
not_repqat = []
repeated = []
for i in Degree:
    if i not in not_repqat:
        not_repqat.append(i)
    else:
        repeated.append(i)

print(tuple(not_repqat))
print(tuple(repeated))