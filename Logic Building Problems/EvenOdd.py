# https://www.geeksforgeeks.org/dsa/check-whether-given-number-even-odd/

def isEven(n):
    rem = n % 2; 
    if rem == 0:
        return True
    else:
        return False

print(isEven(55))
