def store(metric: tuple):
    with open("people.csv","w") as new_file:
        new_file.write(";".join(map(str,metric)) + "\n")


store(("Paul Paulson", 37, 175.5))