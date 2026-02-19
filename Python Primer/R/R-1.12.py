import random

# r = random.choice(s)
s = "Alisher"


total = 0
sequence = []
for i in s:
    total = total + 1
    sequence.append(i)

rr = random.randrange(0, total)

print(sequence[rr])