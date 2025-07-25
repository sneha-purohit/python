# Sum The List

arr = [54, 43, 2, 1, 5]

# First Method
output = sum(arr)
print(output)


# Second Method 

from functools import reduce

arr = [54, 43, 2, 1, 5]

def sum(a,b):
    return a+b

print(reduce(sum, arr))