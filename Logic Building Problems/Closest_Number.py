

def closestNumber ( n, m):
    q = int(n // m)
    left = q * m
    right = (q+1) * m

    if abs(n-left) < abs(right-n):
        return left
    elif abs(n-left) > abs(right-n):
        return right
    elif abs(n-left) == abs(right-n):
        if abs(right) > abs(left):
            return right
        else:
            return left
        
print(closestNumber(-15,6))        
