# 50. Write a Python function to check whether a number is in a given range

# Numbers range are 1 to 50.

input_number = int(input("Enter Number For Check : "))
def checkRange(number):
    if input_number in range(1,51):
        print("Yes",input_number,"is in the Range")
    else:
        print("No",input_number,"is not in Range")

checkRange(input_number)