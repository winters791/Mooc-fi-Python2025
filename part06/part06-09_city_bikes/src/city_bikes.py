import math
def getstation_data(filename: str):
    stations = {}
    with open(f"{filename}") as new_file:
        for lines in new_file:
            parts = lines.strip().split(";")
            if parts[0] == "Longitude":
                continue
            stations[parts[3]] = tuple(parts[0:2])
    return stations

def distances(stations: dict,st1: str, st2: str):
    d1 = []
    d2 = []
    for key, value in stations.items():
        if key == st1:
            d1.append(value)
        if key == st2:
            d2.append(value)
    x_km = (float(d1[0][0]) - float(d2[0][0]))*55.26
    y_km = (float(d1[0][1]) - float(d2[0][1]))*111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


station = getstation_data("stations1.csv")
d = distances(station,"Designmuseo", "Hietalahdentori")
print(d)