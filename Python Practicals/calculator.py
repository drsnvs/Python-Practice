class Calculator:
    def add(self,*num): 
        addition = 0
        for i in num:
            addition += i
        return addition
    def sub(self,num1,num2,*num):
        substraction = num1 - num2
        for i in num:
            substraction -= i
        return substraction
    def mul(self,num1,num2,*num):
        multification = num1 * num2
        for i in num:
            multification *= i
        return multification
    def div(self,num1,num2,*num):
        division = num1 / num2
        for i in num:
            division /= i
        return division

cal = Calculator()
# print(cal.add(10,20,30))
# print(cal.sub(10,20,30))
# print(cal.mul(10,20,30))
# print(cal.div(10,20,30))

inpt = 1

while inpt != 5:
    inpt = int(input("1.Addition\n2.Substraction\n3.Multification\n4.Division\n5.Exit: "))
    if(inpt==1):
        add_inpt = int(input("How many values want to Addition: "))
        lst = list()
        sum = 0
        for i in range(0,add_inpt):
            take = int(input("Enter Number: "))
            lst.append(take)
        for i in lst:
            sum += i
        print(sum)
    elif(inpt==2):
        sub_inpt = int(input("How many values want to Substract: "))
        lst = list()
        sub = 0
        for i in range(0,sub_inpt):
            take = int(input("Enter Number: "))
            lst.append(take)
        for i in lst:
            sub -= i
        print(sub)
