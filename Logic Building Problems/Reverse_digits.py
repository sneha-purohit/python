# https://www.geeksforgeeks.org/dsa/write-a-program-to-reverse-digits-of-a-number/

#def reverse_digits(n):
#     rev = 0
#     while n > 0:
#         a = n % 10
#         rev = rev * 10 + a
#         n = int(n // 10)
#     print(rev)

# reverse_digits(6784965)    
 
 
    
def reverse_digits(n):      
    s = str(n)
    s = list(s)
    s.reverse()
    s = ''.join(s)
    n = int(s)
    return n

print(reverse_digits(76345))


