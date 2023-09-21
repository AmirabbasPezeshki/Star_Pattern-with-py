# start pattern

def counter(input):
    string = ""
    for i in range(input):
        for x in range(input - i):
            string += " "
        for y in range(i * 2 - 1):
            string += '*'
        string += "\n"
    return string

print(counter(12))