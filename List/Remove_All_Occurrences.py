# Remove All Occurrences of an Element
# https://www.geeksforgeeks.org/dsa/remove-element/

arr = [0, 1, 3, 0, 2, 2, 4, 2]
ele = 2


def removeElement(arr, ele):
    k = 0
    for i in range(len(arr)):
        if arr[i] != ele:
            arr[k] = arr[i]
            k += 1
    return k


print(removeElement(arr, ele))

