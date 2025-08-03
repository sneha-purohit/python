# Sum of all Subarrays
# https://www.geeksforgeeks.org/dsa/sum-of-all-subarrays/

arr = [1, 4, 5, 3, 2]

def subarraySum(arr):
    
    n = len(arr)
    result = 0
    for i in range(n):
        result += arr[i] * (i + 1) * (n - i)

    return result

if __name__ == "__main__":
    print(subarraySum(arr))