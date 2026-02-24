
foo = [1, 2, 3]

try:
    if len(foo):
        foo[len(foo)] = ""
except IndexError:
    print("Don't try buffer overflow attacks in Python!")