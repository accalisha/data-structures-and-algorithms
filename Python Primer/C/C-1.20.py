import random

sequence = [1, 2, 3, 4, 5]

#shuffle function
def reorder(n):
    sequence1 = []
    temp_sequence = n.copy()

    for i in range(len(temp_sequence)):
        random_index = random.randint(0, len(temp_sequence) - 1)
        sequence1.append(temp_sequence[random_index])
        temp_sequence.pop(random_index)
        
    return sequence1

print(reorder(sequence))
print(sequence)