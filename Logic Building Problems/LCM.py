# https://www.geeksforgeeks.org/dsa/program-to-find-lcm-of-two-numbers/

def lcm(a, b):
    g = max(a, b) 
    s = min(a, b)  

    for i in range(g, a * b + 1, g):
        if i % s == 0:
            return i
    return a * b 


print(lcm(23,45))