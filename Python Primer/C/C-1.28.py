
#Euclidean norm
def norm(v, p):
    underRoot = 0
    for i in v:
        underRoot += i ** p
    
    return underRoot ** (1 / p)

a = norm([3, 4] , 2)

print(a)