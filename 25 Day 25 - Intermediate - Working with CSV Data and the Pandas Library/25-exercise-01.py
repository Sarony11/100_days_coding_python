""" with open("226 weather-data.csv") as file:
    data = file.readlines()

print(data) """

""" import csv

temperatures = []
with open("226 weather-data.csv") as file:
    data = csv.reader(file)
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except:
            None

    print(temperatures) """

import pandas

data = pandas.read_csv("226 weather-data.csv")

print(sum(data["temp"].tolist())/len(data["temp"].tolist()))
print(data["temp"].mean())

max_temp = data["temp"].max()

print(data[data.temp == max_temp])

