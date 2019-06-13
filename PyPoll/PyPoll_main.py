import csv
import os
import numpy as np

electionfile = os.path.join("Resources", "election_data.csv")

candidates = []
votes = []

filetype = "main"
#Creates dictionary to be used for candidate name and vote count.
poll = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

with open(electionfile, newline="") as csvfile:
    election = csv.reader(csvfile, delimiter=",")
    election_header = next(election)
    
    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    for row in election:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
            
            print(total_votes)
            
#takes dictionary keys and values and, respectively, dumps them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    votes.append(value)

# creates vote percent list
vote_percent = []
for n in votes:
    vote_percent.append(round(n/total_votes*100, 1))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, vote_percent, votes ))
summaries =[]

for row in clean_data:
#     print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
    summary = (row[0] + ": ", str(row[1]) + "%", " (" + str(row[2]) + ")")
    summaries.append(summary)
    print(summaries)


for k in range(len(vote_percent)):
    if votes[k] > votes[k - 1]:
        winner = candidates[k]
        
        
# #creates winner_list to put winners (even if there is a tie)
# winner_list = []

# for name in clean_data:
#     if max(votes) == name[1]:
#         winner_list.append(name[0])

# # makes winner_list a str with the first entry
#  winner = winner_list[0]

# #only runs if there is a tie and puts additional winners into a string separated by commas
# if len(winner_list) > 1:
#     for w in range(1, len(winner_list)):
#         winner = winner + ", " + winner_list[w]
        
        
       #set output destination and write files
output_dest = os.path.join('/Users/hmm794/Documents/Github/Python-Challenge-HM/PyPoll' + str(filetype) + '.txt')

with open(output_dest, 'w') as writefile:
 writefile.writelines('Election Results\n')
 writefile.writelines('----------------------------' + '\n')
    
 writefile.writelines('Total Votes: ' + str(total_votes) + '\n')
 writefile.writelines('----------------------------' + '\n')

 writefile.writelines(str(summaries) + '\n')
 writefile.writelines('----------------------------' + '\n')
 writefile.writelines('Winner: ' + str(winner) + '\n')
    #writefile.writerows([
    
        
# #prints file to terminal
# with open(output_file, 'r') as readfile:
#     print(readfile.read())
