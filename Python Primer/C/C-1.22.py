from array import array

first = array("i", [2, 4, 6, 8, 10, 12])
second = array("i", [1, 3, 5, 7, 9, 11])

#A function that returns the dot product of 2 arrays
def dot(a, b):
    c = array("i", [])

    for i in range(len(a)):
        
        c.append(a[i] * b[i])
    
    return c

print(dot(first, second))