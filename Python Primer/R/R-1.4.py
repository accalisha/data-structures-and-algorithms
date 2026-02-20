def sumOfSquares(n):
    result = 0
    if n <= 0:
        print("A number is not a positive integer")
    else:
        while n != 0:
            n = n - 1
            result = result + n * n
    
    return result

print(sumOfSquares(100000000))