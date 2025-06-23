def file():
    sumlist = {}
    names = {}
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
            sumlist[parts[0]] = sum1
    with open(f"{extra_data}") as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            if parts[0] == "id":
                continue
            sum2 = sum(int(x) for x in parts[1:])
            if parts[0] in sumlist:
                sumlist[parts[0]] += sum2   

    
    
if False:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    extra_data = "exam_points1.csv"
file()