# https://www.geeksforgeeks.org/sum-of-squares-of-first-n-natural-numbers/

def summation(n):
    return sum([i**2 for i in 
               range(1, n + 1)])
 
 
print(summation(10)) 