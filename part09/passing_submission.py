class ExamSubmission:
    def __init__(self, examinee: str,points: int):
        self.examinee = examinee
        self.points = points

def passed(submissions:list,lowest_passing:int):
    passed = []
    for x in submissions:
        if x.points >= lowest_passing:
            passed.append(x.examinee)
    return passed



s1 = ExamSubmission("Peter", 12)
s2 = ExamSubmission("Pippa", 19)
s3 = ExamSubmission("Paul", 15)
s4 = ExamSubmission("Phoebe", 9)
s5 = ExamSubmission("Persephone", 17)

passes = passed([s1, s2, s3, s4, s5], 15)
for passing in passes:
    print(passing)