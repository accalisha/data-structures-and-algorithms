import time
import random

sequence = []
for i in range(1, 16):
    sequence.append(random.randrange(0, 16))
print(sequence)

def is_unique(n):
    iteration = 1
    sameNumbers = []
    
    for i in n:
        for j in range(iteration, len(n)):
            if i == n[j]:
                sameNumbers.append(i)
                for k in range(0, len(sameNumbers) - 1):    #check if the number already in sameNumbers
                    if i == sameNumbers[k]:
                        sameNumbers.pop()

        iteration += 1
        if iteration == len(n):
            if len(sameNumbers) != 0:
                print("There exist same numbers!")
                return sameNumbers
            else:
                print("All numbers are different!")
                return sameNumbers

print(is_unique(sequence))
