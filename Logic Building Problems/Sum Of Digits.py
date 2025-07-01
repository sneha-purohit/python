# https://www.geeksforgeeks.org/program-for-sum-of-the-digits-of-a-given-number/

def sumOfDig(n):
    s = str(n)
    sum = 0
    for ch in s:
        sum += int(ch)

    return sum

print(sumOfDig(67845))