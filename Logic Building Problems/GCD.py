# https://www.geeksforgeeks.org/dsa/program-to-find-gcd-or-hcf-of-two-numbers/

def gcd(a, b):
    result = min(a, b)

    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    return result

print(gcd(45,15))