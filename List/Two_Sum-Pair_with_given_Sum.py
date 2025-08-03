# Two Sum - Pair with given Sum
# https://www.geeksforgeeks.org/dsa/check-if-pair-with-given-sum-exists-in-array/

arr = [0, -1, 2, -3, 1]
target = -2

def twoSum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False

if __name__ == "__main__":
    if twoSum(arr, target):
        print("true")
    else:
        print("false")