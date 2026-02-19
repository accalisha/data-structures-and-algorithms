import time
import random
#Reverse list
listOfIntegers = []
for i in range(1, 10001):
    listOfIntegers.append(random.randrange(0, 10000))


def reverse(n):
    reversedList = []

    start = time.time()
    for i in range(len(n) - 1, -1, -1):
        reversedList.append(listOfIntegers[i])
    end = time.time()

    return reversedList, print(end - start)

def python_reverse(n):
    start = time.time()
    a = reversed(n)
    end = time.time()

    return list(a), print(end - start)

python_reverse(listOfIntegers)
reverse(listOfIntegers)

#Pythons built-in function reversed() is slower for 100000 times than list in 10kk iteration