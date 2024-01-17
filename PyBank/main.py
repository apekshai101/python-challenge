import os
import csv

# Create path for the file
budgetcsv = os.path.join('/Users/apekshaingole/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

# Read the CSV file
with open(budgetcsv) as csvfile:
    csvreader = csv.reader(csvfile)
    
   # Skip the header row 
    csv_header = next(csvfile)
  

    # Initialize Variables
    totalmonths = 0
    finaltotal = 0
    changes = []
    greatestincrease_date = ''
    greatestincrease_value = 0
    greatestdecrease_date = ''
    greatestdecrease_value = 0
    # set variable for profit/loss value
    profitloss = 0

    # Iterate through each row in csvreader  
    for row in csvreader:
        # Calculate total number of months 
        totalmonths = totalmonths + 1
        # Calculate final total by adding profit/loss value to final total during each iteration
        finaltotal = finaltotal + int(row[1])

        # Calculate change by subtracting the previous profit/loss value from current profit/loss value
        if totalmonths > 1:
            change = int(row[1]) - profitloss
        #add the change to the changes list
            changes.append(change)
            
        # Calculate greatest increase/decrease in profit/loss values
            if change > greatestincrease_value:
                greatestincrease_date,greatestincrease_value = row[0], change

            if change < greatestdecrease_value:
                greatestdecrease_date,greatestdecrease_value = row[0], change
                
        # for next iteration, update the profit/loss value with current row value       
        profitloss = int(row[1])

    # Step 7: Display Results to the terminal
    
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months:{totalmonths}")
    print(f"Total:${finaltotal}")
    print(f"Average Change: ${round(sum(changes)/len(changes), 2)}")
    print(f"Greatest Increase in Profits:{greatestincrease_date}(${greatestincrease_value})")
    print(f"Greatest Decrease in Profits:{greatestdecrease_date}(${greatestdecrease_value})")
    
    # Export Results to a Text File
    outputfile = os.path.join("Analysis","analysis.txt")
    with open(outputfile,"w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("-------------------\n")
        txtfile.write(f"Total Months:{totalmonths}\n")
        txtfile.write(f"Total:${finaltotal}\n")
        txtfile.write(f"Average Change: ${round(sum(changes)/len(changes), 2)}\n")
        txtfile.write(f"Greatest Increase in Profits:{greatestincrease_date}(${greatestincrease_value})\n")
        txtfile.write(f"Greatest Decrease in Profits:{greatestdecrease_date}(${greatestdecrease_value})\n")

