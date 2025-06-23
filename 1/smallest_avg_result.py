def smallest_average(person1: dict, person2: dict, person3: dict):
    def average(person):
        return (person["result1"] + person["result2"] + person["result3"]) / 3

    # Compute averages
    avg1 = average(person1)
    avg2 = average(person2)
    avg3 = average(person3)

    # Find and return the person with the smallest average
    if avg1 < avg2 and avg1 < avg3:
        return person1
    elif avg2 < avg3:
        return person2
    else:
        return person3