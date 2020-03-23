# python-challenge
# PyPoll

import csv
import os

# open source file
data_input = os.path.join(".\Resources", "election_data.csv")

# variables
candidate_dict = {}


# loop through data file one row at a time
with open(data_input) as f:
    reader = csv.reader(f)
    next(reader) # skip heading row
    for row in reader:
        candidate = row[2]

        if candidate in candidate_dict:
            candidate_dict[candidate] += 1  # add one to total if candidate already exists
        else:
            candidate_dict[candidate] = 1  # set count to 1 if this is candidate's first vote
    
print(candidate_dict)

# calculate total votes
totalVotes = 0
for key in candidate_dict.keys():
    totalVotes += candidate_dict[key]

# print to terminal and write to file at the same time    
with open("results.txt", 'w') as f:
    print("Election Results")
    f.write("Election Results\n")
    print("-------------------------")
    f.write("-------------------------\n")
    print(f"Total Votes: {totalVotes}")
    f.write(f"Total Votes: {totalVotes}\n")
    print("-------------------------")
    f.write("-------------------------\n")

    # find each candidate name and their vote percentage
    for candidate in candidate_dict.keys():
            print(f"{candidate}: {candidate_dict[candidate]/totalVotes * 100:.3f}% ({candidate_dict[candidate]})")
            f.write(f"{candidate}: {candidate_dict[candidate]/totalVotes * 100:.3f}% ({candidate_dict[candidate]})\n")
    print("-------------------------")
    f.write("-------------------------\n")

    # find winner
    maxVotes = max(candidate_dict.values())
    winner = ""
    for key, value in candidate_dict.items():
        if value == maxVotes:
            winner = key

    print(f"Winner: {winner}")
    f.write(f"Winner: {winner}\n")
    print("-------------------------")
    f.write("-------------------------\n")

