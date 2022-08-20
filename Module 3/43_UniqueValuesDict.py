# 43. Write a Python program to print all unique values in a dictionary.

classes = {
    'aman':50,
    'suraj':60,
    'samir':45,
    'gaurav':49,
    'prince':60,
    'keval':51,
    'chandan':46,
    'tarun':49
}
unique_class = {}
for i,j in classes.items():
    if j not in unique_class.values():
        unique_class.setdefault(i,j)
print(unique_class)