def is_even(k):
    if k == 0:
        return True
    elif k > 0:
        while k > 0:
            k = k - 2
            if k == 0:
                return True
            elif k < 0:
                return False
    elif k < 0:
        while k < 0:
            k = k + 2
            if k == 0:
                return True
            elif k > 0:
                return False
    
a = is_even(-45)
print(a)