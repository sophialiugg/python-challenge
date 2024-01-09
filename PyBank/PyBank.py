import os
import csv


csvpath = os.path.join("Resources", "budget_data.csv")
monthnum = -1
totalProfit = 0
lastprofit = 0
total_profitchange = 0
max_profitchange = 0
min_profitchange = 0
with open(csvpath, encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        monthnum += 1
        if monthnum > 1:
            profitchange = int(row[1]) - lastprofit
            total_profitchange += profitchange
            if profitchange > max_profitchange:
                max_profitchange = profitchange
                max_profitchange_date = row[0]
            if profitchange < min_profitchange:
                min_profitchange = profitchange
                min_profitchange_date = row[0]
        if monthnum != 0:
            totalProfit += int(row[1])
            lastprofit = int(row[1])
profitchange_avg = round(total_profitchange / (monthnum-1),2)
print("Financial Analysis\n----------------------------")
print("Total Months: " + str(monthnum) + "\nTotal: $" + str(totalProfit) + "\nAverage Change: $" + str(profitchange_avg))
print("Greatest Increase in Profits: " + max_profitchange_date + " ($" + str(max_profitchange) + ")")
print("Greatest Decrease in Profits: " + min_profitchange_date + " ($" + str(min_profitchange) + ")")


#Open or if file does not exist then create file named PyBank.txt
with open("PyBank.txt","w") as f: 
    print("Financial Analysis\n----------------------------", file=f)
    print("Total Months: " + str(monthnum) + "\nTotal: $" + str(totalProfit) + "\nAverage Change: $" + str(profitchange_avg), file=f)
    print("Greatest Increase in Profits: " + max_profitchange_date + " ($" + str(max_profitchange) + ")", file=f)
    print("Greatest Decrease in Profits: " + min_profitchange_date + " ($" + str(min_profitchange) + ")", file=f)





