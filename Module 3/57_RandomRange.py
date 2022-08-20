# 57. How can you pick a random item from a range
import random
for i in range(3):
    print(random.randrange(0,100,7))

dict1 = {
    1:'one',
    2:'two',
    3:'three',
    4:'four'
}

for i in range(1):
    print(random.choice(dict1))