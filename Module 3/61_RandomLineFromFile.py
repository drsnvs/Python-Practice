# 61. Write a Python program to read a random line from a file.

import random
def randnum(fname):
	lines=open(fname).read().splitlines()
	print(lines)
	return random.choice(lines)
open("61_RandomLineFromFile.txt")
print(randnum('61_RandomLineFromFile.txt'))