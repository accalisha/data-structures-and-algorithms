def posInt(n):
    TOTAL = 0
    if n > 0:
        for i in range(0, n):
            TOTAL = TOTAL + i*i
    else:
        print("Given number is not positive")
    return(TOTAL)

print(posInt(10))