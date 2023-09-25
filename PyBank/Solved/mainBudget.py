import os
import csv

def budget(data):
    global months
    global netTotal
    global AvgROC
    global AvgROC2
    global AvgROClist 
    global Highest
    global HighM
    global Lowest
    global LowM
    
    months = months + 1
    netTotal = netTotal + int(data[1]) 
    if months == 1:
        AvgROC = int(data[1])
        Highest = int(data[1])
        Lowest = int(data[1])
    elif months > 1:
        AvgROC2 = int(data[1]) - AvgROC
        AvgROClist.append(AvgROC2)
        AvgROC = int(data[1])
        if AvgROC2 > Highest:
                Highest = AvgROC2
                HighM = row[0]
        elif AvgROC2 < Lowest:
                Lowest = AvgROC2
                LowM = row[0]
        
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    months = 0 
    netTotal = 0
    AvgROC = 0
    Highest = 0
    Lowest = 0 
    HighM = ""
    LowM = ""
    AvgROClist = []
    
    
    for row in csvreader:
        budget(row)
    ROC = round(sum(AvgROClist)/(months-1),2)
dict = {'months': months, 
        'Average Change': ROC, 
        'Greatest Increase in Profits': Highest,
        'Greatest Decrease in Profits': Lowest
        }
    
print(f'Financial Analysis')
print(f'--------------------------')
print(f'Total Months: ' + str(months))
print(f'Total: $' + str(netTotal))
print(f'Avgerage Change: $' + str(ROC))
print(f'Greatest Increase in Profits: ' + HighM + " ($" + str(Highest) + ")")
print(f'Greatest Decrease in Profits: ' + LowM + " ($" + str(Lowest) + ")")

output_path = os.path.join("..", "..", "analysis", "budgetcalc.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis')
    txtfile.write('\n')
    txtfile.write('--------------------------')
    txtfile.write('\n')
    txtfile.write('Total Months: ' +str(months))
    txtfile.write('\n')
    txtfile.write('\n')
    txtfile.write('Total: $' + str(netTotal))
    txtfile.write('\n')
    txtfile.write('\n')
    txtfile.write('Average Change: $' + str(ROC))
    txtfile.write('\n')
    txtfile.write('\n')
    txtfile.write('Greatest Increase in Profits: ' + HighM + ' ($' + str(Highest) + ')')
    txtfile.write('\n')
    txtfile.write('\n')
    txtfile.write('Greatest Decrease in Profits: ' + LowM + ' ($' + str(Lowest) + ')')