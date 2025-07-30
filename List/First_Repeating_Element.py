# First Repeating Element
# https://www.geeksforgeeks.org/dsa/find-first-repeating-element-array-integers/

arr= [10, 5, 3, 4, 3, 5, 6]
n = len(arr)

def RepeatingElement(arr):
    for i in range(0,n):
        for j in range(1,n):
            if arr[i] == arr[j]:
                return arr[i]

    return -1

print(RepeatingElement(arr))  
  

