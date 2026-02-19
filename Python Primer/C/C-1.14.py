
sequence = [5, 2, 3, 4, 5, 0, 7, 8]

def productIsOdd(n):
    oddNumbers = []

    for i in n:
        if i % 2 != 0:
            oddNumbers.append(i)
    
    print(oddNumbers)

    if len(oddNumbers) > 0:
        return "There is a distinct numbers whose product is odd"
    else:
        return "Nope"
    
    
print(productIsOdd(sequence))