"""
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


"""

def count_bits(n):
    return bin(n).lstrip("0b").count("1")

count_bits(1234)

#another solutions 

# without using bin(function)

"""

def countBits(n):
    total = 0
    while n > 0:
        total += n % 2
        n >>= 1
    return total

"""