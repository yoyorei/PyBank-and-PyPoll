import os

import csv

date = []

pl = []

csvpath = os.path.join("resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:

        date.append(row[0])

        pl.append((row[1]))

date.pop(0)

pl.pop(0)

total = 0

for num in pl:

    total = total +float(num)

average = (int(pl[len(pl) -1]) - int(pl[0]))/(len(date))

print(len(date))

print(len(pl))

print(total)

print(average)