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

monday = data[data.day == "Monday"]
monday_temp_F = int(monday.temp)*9/5+32
print(monday_temp_F)

# Create DataFrame from scratch
data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data_csv.csv")