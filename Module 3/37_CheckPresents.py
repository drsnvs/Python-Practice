# 37. How Do You Check The Presence Of A Key In A Dictionary?

stock = {
    'tata':1500,
    'reliance':2400,
    'vedanta':267,
    'ptc':200,
    'itc':350,
}

search = input("Enter Stocks you want to Find : ").lower()
if search in stock:
    print("Yes It is Listed.")
else:
    print("No, It is not Listed yet.")