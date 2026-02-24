
order = []

try:
    while True:
        inputs = str(input("Enter something: "))
        order.append(inputs)
except:
    EOFError
    for i in range(len(order) - 1, -1, -1):
        print(order[i])