# 48. Write a Python program to create a dictionary from a string.
# o Note: Track the count of the letters from the string. Sample string:
# 'w3resource'
# o Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

dict1 = {}
words="DarshanBhai"
dict1 = dict1.fromkeys(words)
for i in words:
    new = words.count(i)
    dict1.update({i:new})

print(dict1)