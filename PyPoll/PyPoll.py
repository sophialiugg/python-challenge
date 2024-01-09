import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

votenum = -1
candidate_votenum=0
candidate_list = {}
maxvote = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        votenum += 1
        if  row[2] != "Candidate" and row[2] not in candidate_list:
            candidate_list.update({row[2] : 1})
        elif row[2] != "Candidate":
            candidate_votenum = candidate_list[row[2]] + 1
            candidate_list.update({row[2] : candidate_votenum})  
print("Election Results\n-------------------------")
print("Total Votes: " + str(votenum) + "\n-------------------------")
for candidate in candidate_list:
    candidate_votenum_per = round(candidate_list[candidate]/votenum * 100,3)
    print(candidate + ": " + str(candidate_votenum_per) + "% " + "(" + str(candidate_list[candidate]) + ")")
    if candidate_list[candidate] > maxvote:
        winner = candidate
        maxvote = candidate_list[candidate]
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

with open("PyPoll.txt","w") as f: 
    print("Election Results\n-------------------------", file=f)
    print("Total Votes: " + str(votenum) + "\n-------------------------", file=f)
    for candidate in candidate_list:
        candidate_votenum_per = round(candidate_list[candidate]/votenum * 100,3)
        print(candidate + ": " + str(candidate_votenum_per) + "% " + "(" + str(candidate_list[candidate]) + ")", file=f)
    print("-------------------------", file=f)
    print("Winner: " + winner, file=f)
    print("-------------------------", file=f)

