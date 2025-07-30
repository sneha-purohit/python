# Largest Element
# https://www.geeksforgeeks.org/dsa/program-to-find-largest-element-in-an-array/

arr = [10, 324, 45, 90, 9808]
n = len(arr)

def largest_element(arr,n):
    max = arr[0]

    for i in range(1,n):
        if arr[i] > max:
           max = arr[i]
    return max    

largest_element(arr,n)
print("Largest element is :",largest_element(arr,n))


