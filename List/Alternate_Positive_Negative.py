# Alternate Positive Negative


arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]


def rearrange_alternate(arr):
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]
    
    result = []
    i = j = 0

    while i < len(positives) and j < len(negatives):
        result.append(positives[i])
        result.append(negatives[j])
        i += 1
        j += 1

    while i < len(positives):
        result.append(positives[i])
        i += 1

    while j < len(negatives):
        result.append(negatives[j])
        j += 1

    return result



output = rearrange_alternate(arr)
print(output)  
