
word = str(input("Enter a word: ")).upper()

def vowelCount(n):
    vowels = ["A", "E", "I", "O", "U"]
    NUMBER_OF_VOWELS = 0

    for i in n:
        if i in vowels:
            NUMBER_OF_VOWELS += 1
    
    return NUMBER_OF_VOWELS

print(vowelCount(word))