#Write a program that evaluates an expression given by the user at run time using
#eval () function. Example: Enter and expression: 10+8-9*2-(10*2)
#Result: -20

#expression="10+8-9*2-(10*2)"
#expression = input("Enter Eval Number:")
#print(eval(expression))

A = int(input("A:"))
B = int(input("B:"))
C = int(input("C:"))
D = int(input("D:"))

ans = A+B-C*D-(A*D)

print("Answer is : ",ans)
