# https://www.geeksforgeeks.org/dsa/nth-term-of-ap-from-first-two-terms/

def nthTermOfAP(a1, a2, n):
    nthTerm = a1
    d = a2 - a1
    for i in range(1, n):
        nthTerm += d
    return nthTerm

print(nthTermOfAP(3,7,10))