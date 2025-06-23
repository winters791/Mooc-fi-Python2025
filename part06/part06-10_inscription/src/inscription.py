def inscription():
    x = input("Whom should I sign this to: ")
    y = input("Where shall I save it: ")
    with open(f"{y}","w") as new_file:
        new_file.write(f"Hi {x}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")
inscription()