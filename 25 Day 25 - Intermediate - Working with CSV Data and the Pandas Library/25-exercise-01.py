""" with open("226 weather-data.csv") as file:
    data = file.readlines()

print(data) """

import csv

temperatures = []
with open("226 weather-data.csv") as file:
    data = csv.reader(file)
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except:
            None

    print(temperatures)