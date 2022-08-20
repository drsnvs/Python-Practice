# 41. Write a Python program to map two lists into a dictionary

store = [['one',1],['two',2],['three',3],['four',4],['five',5]]
store_dict = {}
for i in store:
    store_dict.setdefault(i[0],i[1])
print(store_dict)