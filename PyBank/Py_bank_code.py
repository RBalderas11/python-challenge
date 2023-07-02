#Provide the file path to the budget data csv file
file_path = 'C:\Users\Rebecca Balderas\Desktop\unc\projects\python_challenge\budget_data.csv'
budget_data(file_path)

# Import the csv file first
import csv

def budget_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)

# Initialize the variables

    total_months = 0
    net_profit_losses = 0
    prev_profit_loss = 0
    profit_changes = []
    greatest_increase = ["", 0]
    greatest_decrease = ["", 0]

# Pull data from the rows
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
