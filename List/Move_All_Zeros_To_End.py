# Move all zeros to end of array
# https://www.geeksforgeeks.org/dsa/move-zeroes-end-array/

arr = [1, 2, 0, 4, 3, 0, 5, 0]
target = 0

def move_zeros(arr,target):
      
    n = len(arr)
    temp = [0] * n
    j = 0

    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    while j < n:
        temp[j] = 0
        j += 1

    for i in range(n):
        arr[i] = temp[i]

    return arr    

print(move_zeros(arr,target))
