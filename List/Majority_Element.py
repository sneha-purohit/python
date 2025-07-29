# Majority Element
# https://www.geeksforgeeks.org/problems/majority-element-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card&selectedLang=python3

arr = [1, 1, 2, 1, 3, 5, 1]

def majority_element(arr):
    n = len(arr)
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > n // 2:
            return num

    return -1


print("Majority Element:", majority_element(arr))
