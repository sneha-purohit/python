# Missing Number
# https://www.geeksforgeeks.org/dsa/find-the-missing-number/

arr = [8, 2, 4, 5, 3, 7, 1]

def missing(arr):
    n = len(arr) + 1

    totalSum = sum(arr)

    expSum = n * (n+1) // 2
    return expSum - totalSum

print(missing(arr))
