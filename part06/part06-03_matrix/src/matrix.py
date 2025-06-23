def row_sum():
    sums = []
    with open("matrix.txt") as new_file:
        i = 0
        for line in new_file:
            line = line.replace("\n"," ")
            parts = line.split(",")
            for nums in parts:
                i += int(nums)
            sums.append(i)
    return sums

def matrix_max():
    i = 0
    sums = row_sum()
    for x in sums:
        if i < x:
            i = x
    print(i)
def matrix_sum():
    pass

matrix_max()