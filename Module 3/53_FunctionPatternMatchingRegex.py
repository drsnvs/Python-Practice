# 53. How do you perform pattern matching in Python? Explain

import re
def pattern():
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group())

pattern()