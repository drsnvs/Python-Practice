# 56. How can you pick a random item from a list or tuple?

import random
from secrets import choice
numbers_tuple = (1,2,3,4,5,6,7,8,9,10)
numbers_list = [10,20,30,40,50,60,70,80,90,100]

# Generate a random value from the sequence sequence.

print(random.choice(numbers_tuple))
print(random.choice(numbers_list))

print(random.randint(1,100))
print(random.randrange(0,100,2))