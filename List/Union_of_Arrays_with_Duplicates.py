# Union of Arrays with Duplicates
# https://www.geeksforgeeks.org//problems/union-of-two-arrays3538/1&selectedLang=python3

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

def merge_unique_sorted(a, b):
    return sorted(set(a + b))


print(merge_unique_sorted(a, b))



