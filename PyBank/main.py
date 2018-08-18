import os

import csv

date = []

pl = []

csvpath = os.path.join("resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        date.append(row[0])

        pl.append((row[1]))

total = 0

for num in pl:

    total = total +int(num)

average = (int(pl[len(pl) -1]) - int(pl[0]))/(len(date))

max = pl[0]

min = pl[0]

for num in pl:

    if int(num) > int(max):

        max = num
    
    elif int(num) < int(min):

        min = num

maxdate = date[pl.index(max)]

mindate = date[pl.index(min)]

print("")

print("Financial Analysis")

print("--------------------------------------------------")

print("Total Months: "+str(len(date)))

print("Total: " +"$" + str(total))

print("Average Change: " + "$" + str(round(average,2)))

print("Greatest Increase in Profits: " +maxdate + " (" + max + ")")

print("Greatest Decrease in Profits: " +mindate + " (" + min + ")")