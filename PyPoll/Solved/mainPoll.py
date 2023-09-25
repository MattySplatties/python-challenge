import os
import csv

def Poll(data):
    global Votes
    global Candidates
    global CandVotes
    global winnerV
    global winner
    
    Votes = Votes+1
    i = 0
    j = 0
    check = False
    if data[2] not in Candidates:
        Candidates.append(data[2])
        CandVotes.append(1)
    else:
        for Cands in Candidates:
            if check == False:
                if Candidates[i] == data[2]:
                    CandVotes[i] = CandVotes[i] + 1
                    i = 0
                    check = True
                else:
                    i = i + 1
    for cands in CandVotes:
        if cands > winnerV:
            winnerV = cands
            winner = Candidates[j]
        else:
            j = j + 1
        
def percent (info):
    j = 0
    for cand in Candidates:
        x = round((CandVotes[j]/Votes) * 100,3)
        PerVote.append(x)
        j = j +1
        
        
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    Votes = 0
    Candidates = []
    CandVotes = []
    PerVote = []
    winnerV = 0
    winner = ""
    
    for row in csvreader:
        Poll(row)
    percent(Candidates)
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(Votes))
print('-------------------------') 
print(str(Candidates[0]) + " " + str(PerVote[0]) + "% (" + str(CandVotes[0]) + ")")
print(str(Candidates[1]) + " " + str(PerVote[1]) + "% (" + str(CandVotes[1]) + ")")
print(str(Candidates[2]) + " " + str(PerVote[2]) + "% (" + str(CandVotes[2]) + ")")
print('-------------------------')
print("Winner: " + winner)
print('-------------------------')

output_path = os.path.join("..", "..", "analysis", "pollcalc.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results')
    txtfile.write('\n')
    txtfile.write('-------------------------')
    txtfile.write('\n')
    txtfile.write('Total Votes: ' + str(Votes))
    txtfile.write('\n')
    txtfile.write('-------------------------')
    txtfile.write('\n')
    txtfile.write(str(Candidates[0]) + " " + str(PerVote[0]) + "% (" + str(CandVotes[0]) + ")")        
    txtfile.write('\n')
    txtfile.write('\n')
    txtfile.write(str(Candidates[1]) + " " + str(PerVote[1]) + "% (" + str(CandVotes[1]) + ")")
    txtfile.write('\n')
    txtfile.write('\n')
    txtfile.write(str(Candidates[2]) + " " + str(PerVote[2]) + "% (" + str(CandVotes[2]) + ")")        
    txtfile.write('\n')  
    txtfile.write('-------------------------')
    txtfile.write('\n')
    txtfile.write('Winner: ' + winner)