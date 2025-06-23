def largest():
    with open("numbers.txt") as new_file:
        x = 0
        for line in new_file:
            if int(x) < int(line):
                x = line
        print(x)
largest()