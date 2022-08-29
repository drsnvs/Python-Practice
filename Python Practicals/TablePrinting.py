inpt = input("Enter Number you want : ")
lst = []
if inpt.isnumeric():
  inpt = int(inpt)
  for i in range(0,inpt):
    number = input(f"Enter Number {i+1}:")
    if number.isnumeric():
      number = int(number)
      lst.append(number)
    else:
      print("Please Enter Numrice Value for Table\n\tIt will not added in your List")
  print("Your List is :",lst)
  for i in lst:
    print("\nTable of",i,"is below")
    a = f'{i}'
    aa = len(a)+1
    for j in range(1,11):
      d1 = f'{j}'.zfill(2)
      d2 = f'{i*j}'.zfill(aa)
      ans = f'{i} * {d1} = {d2}'
      # print(i,j,i*j)
      print(ans)
else:
  print("Enter Only Numeric Value")
    