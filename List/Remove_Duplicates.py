# Remove Duplicates

arr = [2, 2, 23, 2, 22]

def remove_duplicates(arr):
    a = set()
    result = []
    for num in arr:
        if num not in a:
            a.add(num)
            result.append(num)
    return result


result = remove_duplicates(arr)
print(result)  

