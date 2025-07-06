import math

def isPower(x, y):
    res1 = math.log(y) / math.log(x)
    return res1 == math.floor(res1)

print(isPower(2, 128))