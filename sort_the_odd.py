"""
Task

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

"""


from numpy import sort


def sort_the_odd(n):
    result = n
    even = []
    for i in range(0, len(result)):
        if result[i]%2 != 0:
            even.append(result[i])
            result[i]="x"
    even.sort()
    while len(even) != 0: 
        for i in range(0,len(result)):
            if result[i] == "x":
                result[i] = even[0]
                even.remove(even[0])
    return result
    

sort_the_odd([1,23,5,6,12,8,52])

#totally unhappy with the solution, but at least it works

# another solutions
"""
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]


def sort_array(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]
"""

