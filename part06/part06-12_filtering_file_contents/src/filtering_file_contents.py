import os
def solve(expr):
    if "+" in expr:
        nums = expr.split("+")
        return int(nums[0]) + int(nums[1])
    elif "-" in expr:
        nums = expr.split("-")
        return int(nums[0]) - int(nums[1])
    else:
        return "Invalid expression"


def cater():
    with open("solutions.csv") as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            sol = solve(parts[1])
            print(sol)
            if sol == int(parts[2]):
                with open("correct.csv", "a") as my_file:
                    my_file.write(";".join(parts)+"\n")
            else:
                with open("incorrect.csv", "a") as my_file:
                    my_file.write(";".join(parts) + "\n")
os.remove("solutions.csv")
os.remove("incorrect.csv")

cater()