# 47. Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
# o {'item': 'item1', 'amount': 750}]
# o Expected Output: Counter ({'item1': 1150, 'item2': 300})

student_data = [
    {
        'name':'Darshan',
        'roll_no':1
    },
    {
        'name':'ritik',
        'roll_no':2
    },
    {
        'name':'karan',
        'roll_no':3
    },
    {
        'name':'jay',
        'roll_no':4
    },
    {
        'name':'jigar',
        'roll_no':5
    }
]

dict_data = {}
for i in range(0,len(student_data)):
    # print(student_data[i]['name'],student_data[i]['roll_no'])
    dict_data.setdefault(student_data[i]['name'],student_data[i]['roll_no'])

print(dict_data)