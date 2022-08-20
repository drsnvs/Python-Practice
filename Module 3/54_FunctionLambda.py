# 54. What is lambda function in python? What we call a function which is incomplete version of a function?

# Lambda Function, also referred to as 'Anonymous function' is same as a regular python function but can be defined without a name. While normal functions are defined using the def keyword, anonymous functions are defined using the lambda keyword. However,they are restricted to single line of expression.

# Add 10 to argument a, and return the result:
lmd = lambda l:10+l
print("One Argument:",lmd(10))

# Multiply argument a with argument b and return the result:
lmd = lambda l,m : l+m
print("Two Argument:",lmd(10,20))
lmd = lambda l,m,d : l+m+d
print("Three Argument:",lmd(10,20,30))

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def sum(b):
    return lambda a : a*b
ans = sum(10) # Take 'b' as a Argument
print("Use of Lambda in Function:",ans(10)) # Take 'a' as a Argument