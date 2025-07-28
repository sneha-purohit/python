# Array Leaders
# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card&selectedLang=python3

arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
def find_leaders(arr):
    leaders = []
    max_so_far = float('-inf')
    
    for num in reversed(arr):
        if num > max_so_far:
            leaders.append(num)
            max_so_far = num
    
    return leaders[::-1]

print(find_leaders(arr)) 