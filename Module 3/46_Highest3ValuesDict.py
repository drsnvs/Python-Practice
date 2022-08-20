# 46. Write a Python program to find the highest 3 values in a dictionary

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
# list1 = list(classes.values())
# print(list1)
# list1.sort()
# print(list1)
sorting = list(classes.values())
sorting.sort()
print(sorting)

print('Highest 3 Values are',sorting[0:3:1])