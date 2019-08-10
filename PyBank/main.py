import os
import csv

cwkdir = os.getcwd()
filepath = os.path.join(cwkdir,'Resources','budget_data.csv')

month_count = 0; total = 0; Value = 0; Diff = 0; Max = 0; Min = 0

with open(filepath, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     csv_header = next(csvreader)
     print(f'Financial Analysis'+'\n')
     print(f'----------------------------'+'\n')
     for i in csvreader:
         month = i[0]
         Amount = i[1]
         iAmount = int(Amount)
         Diff =  iAmount - Value
         #Profit increase
         if Max < Diff:
            Max = Diff
            MaxDate = month
         #Profit decrease
         if Min > Diff:
            Min = Diff
            MinDate = month

         Value = iAmount   
         # Get total months (financial analysis)
         month_count = month_count + 1
         total += int(Amount) 
    

print(f'Total Months : {month_count}')

print(f'Total: $ {total}')

print(f'Greatest Increase in Profits: {MaxDate} : ($ {Max})')

print(f'Greatest Decrease in Profits: {MinDate} : ($ {Min})')