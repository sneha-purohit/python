# https://www.geeksforgeeks.org/dsa/introduction-to-primality-test-and-school-method/


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("true") if isPrime(16) else print("false")
