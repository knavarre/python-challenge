#PyBank Outputs
    # Total Months: number 
    # Total: amount 
    # Average Change: amount 
    # Greatest Increase in Profits: Month-Day (amount)
    # Greatest Decreaase in Profits: Month-Day (amount)

#import dependencies
import os
import csv

#CSV file path
csvpath = os.path.join('python-challenge','PyBank','Resources','budget_data.csv')

#create empty lists
months = []
profit = []
changes = []

# create variables
counter = 0
initial = 0
maxvalue = 0
minvalue = 0 
minchange = 0
maxchange = 0
change = 0


#open file and specify delimiter = ',' 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # denote csv header
    csv_header = next(csvreader)

    #Total Months & Total Profit/Loss Amount 
    for row in csvreader:

        # increase counter value 
        counter +=1

        # make list including all months 
        months.append(row[0])

        # make list including all profit/loss
        profit.append(int(row[1]))

        # set initial profit/loss value 
        if counter == 1:
            initial = int(row[1])

        else:
            # make list including all changes 
            change = int(row[1])-initial
            changes.append(change)
            initial = int(row[1])

            # Decrease in Profits (value and month)
            if change < minchange:
                minchange = change
                minmonth = row[0]
        
            # Increase in Profits (value and month)
            if change > maxchange:
                maxchange = change
                maxmonth = row[0]
            

# print results
print("Financial Analysis")
print("--------------------------------")
print("Total Months:"+ str(len(months)))
print("Total: $" + str(sum(profit)))
print("Average Change: $" + str(round(sum(changes)/int(len(changes)),2)))
print("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxchange) + ")")
print("Greatest Decrease in Profits: " + minmonth + " ($" + str(minchange) + ")")

# Export results to analysis folder
output_path = os.path.join('python-challenge','PyBank','analysis','analyzed_budget_data.txt')

with open(output_path, "w") as file:
    file.write("Financial Analysis" + '\n')
    file.write("--------------------------------" + '\n')
    file.write("Total Months:"+ str(len(months)) + '\n')
    file.write("Total: $" + str(sum(profit)) + '\n')
    file.write("Average Change: $" + str(round(sum(changes)/int(len(changes)),2)) + '\n')
    file.write("Greatest Increase in Profits: " + maxmonth + " ($" + str(maxchange) + ")" + '\n')
    file.write("Greatest Decrease in Profits: " + minmonth + " ($" + str(minchange) + ")" + '\n')

file.close()