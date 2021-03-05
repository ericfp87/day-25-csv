# with open("./weather_data.csv", "r") as data_values:
#     data = []
#     for value in data_values:
#         data.append(data_values.readlines())
#     print(data)
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)