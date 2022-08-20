# 52. Write a Python function that checks whether a passed string is palindrome or not

Name = "volov"
def palindrome(Name):
    left = 0
    right = len(Name)-1
    while right>=left:
        if not Name[left] == Name[right]:
            return False
        left += 1
        right -= 1
    return True
    
print(palindrome(Name))