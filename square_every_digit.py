"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer

"""

def every_square_digit(n):
    results = ""
    for i in str(n):
        results += str(int(i)**2)
    return int(results)


every_square_digit(9119)

# my solution was on top

# another 

"""
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

"""