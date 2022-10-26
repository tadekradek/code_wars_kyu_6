
"""

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
Example

create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.

Don't forget the space after the closing parentheses!


"""

def create_phone_number(n):
    phone_number = ""
    for i in n:
        phone_number += str(i)
    return f"({phone_number[0:3]}) {phone_number[3:6]}-{phone_number[6:10]}"

create_phone_number([0,1,2,3,4,5,6,7,8,9])


"radek tadek {}".format(*[0,1,2,3,4,5,6,7,8,9])

#another solutions

"""
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number(n):
    n = ''.join(map(str,n))
    return '(%s) %s-%s'%(n[:3], n[3:6], n[6:])


"""

