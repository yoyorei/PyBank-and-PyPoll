import os

import csv

date = []

pl = []

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:

        date.append(row[0])

        pl.append((row[1]))

total = 0

for num in pl:

    total = total +int(num)

average = (int(pl[len(pl) - 1]) - int(pl[0]))/(len(date) - 1)

max = int(pl[1]) - int(pl[0])

min = int(pl[1]) - int(pl[0])

for i in range(len(pl) - 1):

    if int(pl[i + 1]) - int(pl[i]) > max:

        max = int(pl[i + 1]) - int(pl[i])
        
        maxdate = date[i + 1]
    
    elif int(pl[i + 1]) - int(pl[i]) < min:

        min = int(pl[i + 1]) - int(pl[i])

        mindate = date[i + 1]

print("")

print("Financial Analysis")

print("--------------------------------------------------")

print("Total Months: "+str(len(date)))

print("Total: " +"$" + str(total))

print("Average Change: " + "$" + str(round(average,2)))

print("Greatest Increase in Profits: " + str(maxdate) + " ($" + str(max) + ")")

print("Greatest Decrease in Profits: " + str(mindate) + " ($" + str(min) + ")")

print("")


output_path = os.path.join("financial_analysis.txt")

with open(output_path, "w", newline="") as txt:

    txt.write("Financial Analysis\n")

    txt.write("--------------------------------------------------\n")

    txt.write("Total Months: "+str(len(date)) + "\n")

    txt.write("Total: " +"$" + str(total) + "\n")

    txt.write("Average Change: " + "$" + str(round(average,2)) + "\n")

    txt.write("Greatest Increase in Profits: " + str(maxdate) + " ($" + str(max) + ")\n")

    txt.write("Greatest Decrease in Profits: " + str(mindate) + " ($" + str(min) + ")")