def sys():
    x = input("1 - add an entry, 2 - read entries, 0 - quit: ")
    if int(x) == 1:
        y = input("Enter: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(y)
            my_file.write("\n")
    if int(x) == 2:
        with open("diary.txt") as new_file:
            for line in new_file:
                print(line)
    if int(x) == 0:
        return 1
    else:
        return 0

sys()