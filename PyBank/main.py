#make lists and variables
months = []
profit_loss = []
average_change =[]

total_revenue = 0
filetype = "main"
#read-in file and do stats

with open('budget_data.csv') as file:
    Pybank = csv.reader(file)
    if csv.Sniffer().has_header:
        next(Pybank)
        
    for row in Pybank:
        months.append(row[0])
        profit_loss.append(int(row[1]))
        
#find total months
total_months = len(months)
print("Total_months " +  str(total_months))

     # sum of revenue

for i in profit_loss:
    total_revenue += int(i)

print("Net Total amount: $" + str(total_revenue))

# find average change
total_change = 0
for r in range(1, len(profit_loss)):
    average_change.append(int(profit_loss[r]) - int(profit_loss[r - 1]))
    
avg_change = sum(average_change)/len(average_change)

print("Average Profit/Loss Change: $" + str(round(avg_change,2)))
    
# greatest increase in profit/loss

GI_profit= 0
for j in range(len(profit_loss)):
    if int(profit_loss[j]) - int(profit_loss[j - 1]) > GI_profit:
        GI_profit = int(profit_loss[j]) - int(profit_loss[j - 1])
        GI_month = months[j]

print("Greatest Increase in Profits:", GI_month, "($" + str(GI_profit) + ")")

# greatest decrease in profit/loss
GD_profit= 0
for k in range(len(profit_loss)):
    if int(profit_loss[k]) - int(profit_loss[k - 1]) < GD_profit:
        GD_profit = int(profit_loss[k]) - int(profit_loss[k - 1])
        GD_month = months[k]

print("Greatest Decrease [GD]in Profits:", GD_month, "($" + str(GD_profit) + ")")

#set output destination and write files
output_dest = os.path.join('/Users/hmm794/Documents/Github/Python-Challenge-HM/PyBank' + str(filetype) + '.txt')

with open(output_dest, 'w') as writefile:
   writefile.writelines('Financial Analysis\n')
   writefile.writelines('----------------------------' + '\n')
   writefile.writelines('Total Months: ' + str(total_months) + '\n')
   writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
   writefile.writelines('Average Revenue Change: $' + str(round(avg_change,2)) + '\n')
   writefile.writelines('Greatest Increase in Profits: ' + GI_month + ' ($' + str(GI_profit) + ')'+ '\n')
   writefile.writelines('Greatest Decrease in Revenue: ' + GD_month + ' ($' + str(GD_profit) + ')')
    
    