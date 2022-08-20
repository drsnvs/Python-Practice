# 26. Write a Python program to reverse a tuple.

Days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

# 1'st Method: 
for i in range(len(Days)-1,-1,-1):
    print(Days[i],end=' ')
print()
print()

# 2'nd Method:
Days = list(Days)
Days.reverse()
for i in Days:
    print(i,end=' ')