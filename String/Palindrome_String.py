# Palindrome String
# https://www.geeksforgeeks.org/dsa/palindrome-string/

s = "abba"

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return 0

        left += 1
        right -= 1

    return 1

print(is_palindrome(s))
