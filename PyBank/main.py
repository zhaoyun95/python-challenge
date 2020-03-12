# python-challenge
# PyBank

import csv
import os

# data file
data_input = os.path.join(".\Resources", "budget_data.csv")

# 3 lists to hold data
dates = []
profits = []
changes = [] # for increase and decease in profits

# loop through the data file one row at a time
with open(data_input) as f:
    reader = csv.reader(f)
    header = True
    for row in reader:
        if header: # skip header line
            header = False
        else:
            dates.append(row[0])
            profits.append(int(row[1]))
            if len(dates)>1:  # 1st one has no change, so skip it.
                changes.append(profits[-1] - profits[-2])
# debug prints
# print(dates)
# print(profits)
# print(changes)

# get statistics
averageChange = sum(changes)/len(changes)
maxIncrease = max(changes)
maxDecrease = min(changes)

# need to add 1 to the index since changes started at 2nd profit/loss
maxIncreaseDate = dates[changes.index(maxIncrease) + 1]
maxDecreaseDate = dates[changes.index(maxDecrease) + 1]


# print to the terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(dates)}")
print(f"Total: ${sum(profits)}")
print(f"Average Change: ${averageChange:.2f}")
print(f"Greatest Increase in Profits: {maxIncreaseDate} (${maxIncrease})")
print(f"Greatest Decrease in Profits: {maxDecreaseDate} (${maxDecrease})")

# write to a text file
with open("results.txt", 'w') as f:
    f.write("Financial Analysis\n")  # must add newline character(\n) at the end
    f.write("-----------------------------\n")
    f.write(f"Total Months: {len(dates)}\n")
    f.write(f"Total: ${sum(profits)}\n")
    f.write(f"Average Change: ${averageChange:.2f}\n")
    f.write(f"Greatest Increase in Profits: {maxIncreaseDate} (${maxIncrease})\n")
    f.write(f"Greatest Decrease in Profits: {maxDecreaseDate} (${maxDecrease})\n")    






    
