def posInt(n):
    TOTAL = 0
    if n > 0:
        for i in range(0, n):
            if i % 2 != 0:
                TOTAL = TOTAL + i*i
        return TOTAL
    else:
        print("Given number is not positive")
        
    

print(posInt(5))