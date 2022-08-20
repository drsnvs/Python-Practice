# 35. Write a Python script to check if a given key already exists in a dictionary.

fruits = {
    'appple':50,
    'banana':20,
    'orange':60,
    'graps':70,
    'kiwi':80,
}

search = input("Enter for searching fruits: ").lower()

if search in fruits:
    print("Yes",search,"is available for",fruits[search],"Rupees.")
else:
    print("No",search,"is not available.")