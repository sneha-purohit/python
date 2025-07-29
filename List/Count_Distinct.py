# Count Distinct
# https://www.geeksforgeeks.org//problems/count-distinct/1&selectedLang=python3

arr = [2, 3, 4, 5, 1, 2, 14, 6, 8, 7, 5]

def count_distinct(arr):
    return len(set(arr))


print("Number of distinct elements:", count_distinct(arr))