# Second Largest Element
# https://www.geeksforgeeks.org/dsa/find-second-largest-element-array/


arr = [12, 35, 1, 10, 34, 1]

def secondlargest(arr):
    n = len(arr)
    arr.sort()

    for i in range(n-2,-1,-1):
        if arr[i] != arr[n-1]:
            return arr[i]
        
    return -1
    
print(secondlargest(arr))