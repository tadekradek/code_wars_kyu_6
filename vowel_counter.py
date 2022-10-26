def get_count(sentence):
    counter = 0
    for i in sentence:
        if i in ("a","e","i","o","u"):
            counter +=1
    return counter

"x" in ("x","y","t","z")

# other solutions

"""
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU") ## shows that 


import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE))

"""