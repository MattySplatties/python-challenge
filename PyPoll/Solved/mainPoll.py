import os
import csv

def Poll(data):
    #Global Variables
    global Votes
    global Candidates
    global CandVotes
    global winnerV
    global winner
    
    #tracks votes, and i and j are itteraters
    Votes = Votes+1
    i = 0
    j = 0
    check = False # prevents incorrect total of first candidate votes
    if data[2] not in Candidates: # adds canidate not in list
        Candidates.append(data[2])
        CandVotes.append(1)
    else:
        for Cands in Candidates:
            if check == False:
                if Candidates[i] == data[2]: #keeps track of canidate votes
                    CandVotes[i] = CandVotes[i] + 1
                    i = 0
                    check = True #kicks out of if for current line
                else:
                    i = i + 1 #goes through the the candidates list to check
                    
    for cands in CandVotes: #tracks who the winner is at the end
        if cands > winnerV:
            winnerV = cands
            winner = Candidates[j]
        else:
            j = j + 1
        
def percent (info): #simple program that calculates percent for each canidate
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
    
    #rights to terminal
    for row in csvreader:
        Poll(row)
    percent(Candidates)
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(Votes))
print('-------------------------') 
print(str(Candidates[0]) + " " + str(PerVote[0]) + "% (" + str(CandVotes[0]) + ")")
print('-------------------------') 
print(str(Candidates[1]) + " " + str(PerVote[1]) + "% (" + str(CandVotes[1]) + ")")
print('-------------------------') 
print(str(Candidates[2]) + " " + str(PerVote[2]) + "% (" + str(CandVotes[2]) + ")")
print('-------------------------')
print("Winner: " + winner)
print('-------------------------')


#creates and writes to text file
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
    txtfile.write('-------------------------')
    txtfile.write('\n')
    txtfile.write(str(Candidates[1]) + " " + str(PerVote[1]) + "% (" + str(CandVotes[1]) + ")")
    txtfile.write('\n')
    txtfile.write('-------------------------')
    txtfile.write('\n')
    txtfile.write(str(Candidates[2]) + " " + str(PerVote[2]) + "% (" + str(CandVotes[2]) + ")")        
    txtfile.write('\n')  
    txtfile.write('-------------------------')
    txtfile.write('\n')
    txtfile.write('Winner: ' + winner)