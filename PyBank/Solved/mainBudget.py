import os
import csv

def budget(data):
    #set of global variables that can be called out of function
    global months
    global netTotal
    global AvgROC
    global AvgROC2
    global AvgROClist 
    global Highest
    global HighM
    global Lowest
    global LowM
    
    months = months + 1 #month count
    netTotal = netTotal + int(data[1]) #tracks net total
    if months == 1: #sets all these variables for ONLY the first month
        AvgROC = int(data[1])
        Highest = int(data[1])
        Lowest = int(data[1])
    elif months > 1: #runs the rest of the time, which is not the first month
        AvgROC2 = int(data[1]) - AvgROC
        AvgROClist.append(AvgROC2)
        AvgROC = int(data[1])
        if AvgROC2 > Highest: #checkest for the highest change, and keeps track of date
                Highest = AvgROC2
                HighM = row[0]
        elif AvgROC2 < Lowest: #same for lowest
                Lowest = AvgROC2
                LowM = row[0]
        
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    #variables in def that will be called
    months = 0 
    netTotal = 0
    AvgROC = 0
    Highest = 0
    Lowest = 0 
    HighM = ""
    LowM = ""
    AvgROClist = []
    
    
    for row in csvreader:
        budget(row) # runs through all rows
    ROC = round(sum(AvgROClist)/(months-1),2) #calucaltes the average of the ROC

# printing for the command propmt
print('Financial Analysis')
print('--------------------------')
print('Total Months: ' + str(months))
print('--------------------------')
print('Total: $' + str(netTotal))
print('--------------------------')
print('Avgerage Change: $' + str(ROC))
print('--------------------------')
print('Greatest Increase in Profits: ' + HighM + " ($" + str(Highest) + ")")
print('--------------------------')
print('Greatest Decrease in Profits: ' + LowM + " ($" + str(Lowest) + ")")


#path and writing to text file in analysis
output_path = os.path.join("..", "..", "analysis", "budgetcalc.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis')
    txtfile.write('\n')
    txtfile.write('--------------------------')
    txtfile.write('\n')
    txtfile.write('Total Months: ' +str(months))
    txtfile.write('\n')
    txtfile.write('--------------------------')
    txtfile.write('\n')
    txtfile.write('Total: $' + str(netTotal))
    txtfile.write('\n')
    txtfile.write('--------------------------')
    txtfile.write('\n')
    txtfile.write('Average Change: $' + str(ROC))
    txtfile.write('\n')
    txtfile.write('--------------------------')
    txtfile.write('\n')
    txtfile.write('Greatest Increase in Profits: ' + HighM + ' ($' + str(Highest) + ')')
    txtfile.write('\n')
    txtfile.write('--------------------------')
    txtfile.write('\n')
    txtfile.write('Greatest Decrease in Profits: ' + LowM + ' ($' + str(Lowest) + ')')