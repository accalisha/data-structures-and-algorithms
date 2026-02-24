
s = str(input("Enter a sentence: "))

def removedPunctuations(n):
    copy = ""
    not_punctuations = [" "]
    for i in range(ord('a'), ord('z') + 1):
        not_punctuations.append(chr(i))
    
    for i in range(ord('A'), ord('Z') + 1):
        not_punctuations.append(chr(i))

    for i in range(0, 10):
        not_punctuations.append(chr(i))

    for i in n:
        if i in not_punctuations:
            copy += i
    
    return copy

print(removedPunctuations(s))