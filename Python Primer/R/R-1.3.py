

def minmax(data):
    k = -1
    minimum = data[0]
    maximum = data[0]
    for i in data:
        k = k + 1
        if data[k] < minimum:
            minimum = data[k]
    k = -1
    
    for j in data:
        k = k + 1
        if data[k] > maximum:
            maximum = data[k]
    return (minimum, maximum)

print(minmax([123, 422, 13, -14, 5, 46, 7]))