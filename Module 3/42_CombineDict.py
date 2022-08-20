# 42. Write a Python program to combine two dictionary adding values for common keys.
# o d1 = {'a': 100, 'b': 200, 'c':300}
# o d2 = {'a': 300, 'b': 200,’d’:400}

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200,'d':400}
# d1.update(d2)
# print(d1)
for i in d2:
    if i not in d1:
        d1.setdefault(i,d2[i])
        d2.pop(i)
        break
for i in d1:
    if i in d2:
        d1[i]=(d1[i]+d2[i])
print(d1)
# d1.update(d2)
# print(d1)