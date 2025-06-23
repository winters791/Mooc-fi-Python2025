def file():
    names = {}
    exercises = {}
    with open(f"{student_info}") as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            if parts[0] == "id":
                continue
            names[f"{parts[0]}"] = parts[1]+ " "+ parts[2]
    with open(f"{exercise_data}") as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            if parts[0] == "id":
                continue
            sum1 = sum(int(x) for x in parts[1:])
            exercises[parts[0]] = sum1
    for id,name in names.items():
        if id in exercises:
            print(f"{name} {exercises[id]}")
    


if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
file()