# Import the necessary libraries
import os
import csv

# Print the title of the analysis
print("Financial Analysis")
print("----------------------------------")


# Create the path to the CSV file
csv_path = os.path.join('Resources', 'budget_data.csv')

# Open and read the CSV file
with open(csv_path, 'r') as bank_data:
    bank_data_reader = csv.reader(bank_data)
    
    next(bank_data_reader)

    bank_data_list = list(bank_data_reader)
    Total_Profit = 0
    
    # Calculate the total profit by summing the values in the second column of the CSV
    for row in bank_data_list:
        Total_Profit += int(row[1])

# Print the total number of months and total profit
print("Total Months:", len(bank_data_list))
print("Total :$", Total_Profit)

# Initialize empty lists to store months and revenue
months = []
revenue = []

# Read the CSV file again to extract months and revenue data
with open(csv_path, 'r') as bank_data:
    bank_data_reader = csv.reader(bank_data)

    for row in bank_data_reader:
        months.append(row[0])
        revenue.append(row[1])

# Convert revenue values to floats and remove the header row
revenue = [float(number) for number in revenue[1:]]
months = [date for date in months[1:]]

# Initialize variables for tracking profit changes and the greatest increase and decrease
profit_lastmon = 0
change_sum = [0]

# Calculate profit changes and store them in the change_sum list
for i in range(1, len(revenue)):
    profit_current = float(revenue[i])
    change_mtm = profit_current - profit_lastmon
    change_sum.append(change_mtm)
    profit_lastmon = profit_current

# Find the index of the greatest increase and decrease in profits
greatest_increase = change_sum.index(max(change_sum))
greatest_decrease = change_sum.index(min(change_sum))

# Print the average change, greatest increase, and greatest decrease in profits
print("Average Change: $", (sum(change_sum) / len(change_sum)))
print("Greatest Increase in Profits:", months[greatest_increase], max(change_sum))
print("Greatest Decrease in Profits:", months[greatest_decrease], min(change_sum))

# Write the results to a text file
with open('Result_Pybank.txt', 'w') as text:
    text.write('Financial Analysis\n')
    text.write('-------------------------\n')
    text.write(f"Total Months: {len(bank_data_list)}\n")
    text.write(f"Total :${Total_Profit}\n")
    text.write(f"Average Change: $ {(sum(change_sum) / len(change_sum))}\n")
    text.write(f"Greatest Increase in Profits: {months[greatest_increase], max(change_sum)}\n")
    text.write(f"Greatest Decrease in Profits: {months[greatest_decrease], min(change_sum)}")
