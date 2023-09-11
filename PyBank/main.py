
import os
import csv



#get working directory path
cwd = os.getcwd()

#create path to budget_data.csv
csvpath = os.path.join(cwd, 'Resources', 'budget_data.csv')


#Open the csv file
with open(csvpath, encoding='utf-8') as csvfile:
           
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Store the first row of the csv and then advance to the next row
    column_headers = next(csvreader)
    
    #Create empty lists for dates column, profit/loss column, and changes in profit/loss
    dates_list =[]
    profit_loss_list = []
    changes = []
    
    #read the elements from the csv into their respective lists
    for row in csvreader:
        dates_list.append(row[0])
        profit_loss_list.append(int(row[1]))

    #get total months by getting length of the dates_list
    total_months = len(dates_list)

    #get net_pl (net total amount of "Profit/Losses") by getting sum of profit_loss_list
    net_pl = sum(profit_loss_list)
    
    #create changes list by subtracting next month profit/loss from previous except on the initial month so start at index=1
    for element in range(1, total_months):
        
        changes.append(profit_loss_list[element] - profit_loss_list[element - 1])
    
    # (1) calculate and round the average change to two decimal points
    avg_change = round((sum(changes) / len(changes)),2)
    
    #calculate greatest increase in profits by taking the max of the changes list
    greatest_increase = max(changes)
    #pull the date of the greatest increase by pulling index of the max value in changes and add 1 to that index 
    #add 1 to the index because 'changes' skipped the initial month so list is 1 element shorter
    greatest_increase_date = dates_list[changes.index(max(changes)) + 1]

    #calculate greatest decrease in profits by taking the min of the changes list
    greatest_decrease = min(changes)
    #pull the date of the greatest decrease by pulling index of the min value in changes and add 1 to that index 
    #add 1 to the index because 'changes' skipped the initial month so list is 1 element shorter
    greatest_decrease_date = dates_list[changes.index(min(changes)) + 1]



#create a function that will both print and write to a file this way we dont have to repeat both the print and write statements
def print_and_write(filename, string):
    filename.write(string + "\n")
    print(string)

output_path = os.path.join(cwd, 'analysis', 'Financial_Analysis.txt' )

#write to a file and print results using the function you created
with open(output_path, 'w') as file:
    print_and_write(file, "Financial Analysis\n")
    print_and_write(file, "----------------------------\n")
    print_and_write(file, f'Total Months: {total_months}\n')
    print_and_write(file, f'Total: ${net_pl}\n')
    print_and_write(file, f'Average Change: ${avg_change}\n')
    print_and_write(file, f'Greatest Increase in Profits: {greatest_increase_date} (${int(greatest_increase)})\n')
    print_and_write(file, f'Greatest Decrease in Profits: {greatest_decrease_date} (${int(greatest_decrease)})\n')

    
    




