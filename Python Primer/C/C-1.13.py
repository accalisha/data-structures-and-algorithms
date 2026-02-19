#Reverse list
listOfIntegers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverse(n):
    reversedList = []
      
    for i in range(len(n) - 1, -1, -1):
        reversedList.append(listOfIntegers[i])
    
    return reversedList

print(reverse(listOfIntegers))