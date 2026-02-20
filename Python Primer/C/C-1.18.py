#Produce list
sequence = []

for i in range(0, 10):
    sequence.append(i * (i + 1))

print(sequence)

sequence1 = [x * (x + 1) for x in range(0, 10)]
print(sequence1)