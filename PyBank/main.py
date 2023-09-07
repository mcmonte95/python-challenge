
import os
import csv
import pandas as pd
import numpy as np


#get working directory path
cwd = os.getcwd()

#create path to budget_data.csv
csvpath = os.path.join(cwd, 'Resources', 'budget_data.csv')


#read csv into a pandas dataframe
budget_df = pd.read_csv(csvpath)

#sum up net profit/loss from "Profit/Losses" column of the dataframe
net_pl = budget_df['Profit/Losses'].sum()

# (1) create a new column in the dataframe that calculates the changes over each period by using the 'shift' method
# first row of this new column will be #N/A since we cant compare the first value since its the initial value
budget_df['changes'] = budget_df['Profit/Losses'] - budget_df['Profit/Losses'].shift() 
budget_df = budget_df.fillna("#N/A")

#find total months by getting length of the Date column
total_months = len(budget_df['Date'])

#calculate the average change by calling the mean method in pandas
#using iloc to exclude the first row of the 'changes' column since this is the initial value and is #N/A
avg_change = budget_df['changes'].iloc[1:].mean()

# (2) round the avearge change to two decimal points
avg_change = round(avg_change, 2)

# finding greatest increase calling 'max' on the changes column excluding the first row 
greatest_increase = budget_df['changes'].iloc[1:].max()

# (3) finding the date of greatest increase by calling 'idxmax' method on the 'changes' column to grab the row index then using iloc to locate the date in column 'Date'
# need to use 'astype(float)' since 'idxmax' wont work on a series object 
greatest_increase_date = budget_df['Date'].iloc[budget_df['changes'].iloc[1:].astype(float).idxmax()]

# finding greatest decrease calling 'min' on the changes column excluding the first row 
greatest_decrease = budget_df['changes'].iloc[1:].min()

# (3) If there is an 'idxmax' we can assume an 'idxmin' method also exists call that in the same way to find index of greatest decrease
# need to use 'astype(float)' since 'idxmin' wont work on a series object 
greatest_decrease_date = budget_df['Date'].iloc[budget_df['changes'].iloc[1:].astype(float).idxmin()]


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

    
    




