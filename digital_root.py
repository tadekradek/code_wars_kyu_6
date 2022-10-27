"""
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


"""

# my working solution

def digital_root(n):
    if len(str(n)) != 1:
        val = 0
        for i in str(n):
            val += int(i)
        if len(str(val)) == 1:
            return val
        else:
            return digital_root(val)

    else:
        return n

# another solutions

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# superclever solution, map function ->make an iterator that computes the function using arguments from each of the iterables


def digital_root(n):
    return n%9 or n and 9 

# that clever that I had to check whats going on
