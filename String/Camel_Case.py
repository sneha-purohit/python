# Camel Case
# https://www.geeksforgeeks.org/dsa/camel-case-given-sentence/

s = "here comes the garden"

def convertToCamelCase(s):
    res = []
    capitalizeNext = False

    for i in range(len(s)):
        if s[i] == ' ':
            capitalizeNext= True

        elif capitalizeNext:
            res.append(s[i].upper()) 

            capitalizeNext = False

        else:
            res.append(s[i])

    return ''.join(res)

print(convertToCamelCase(s))               