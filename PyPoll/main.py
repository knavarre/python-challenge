#PyPoll
    # Total Votes: total
    # List of Canditates who recieved Votes 
        # With percentage of votes won/candiate
        # With total number of votes/candidate
    # Winner of the election based on popular vote 

# import dependencies
import os
import csv

# CSV file path
csvpath = os.path.join('python-challenge','PyPoll','Resources','election_data.csv')

# create empty lists
ballots = []
candidates = []
results = []
final_results = []

# create empty dictionary
votes = {}

# create variables
last_count = 0
winner = ""

# open file and specify dellimiter = ',' 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    # denote csv header
    csv_header = next(csvreader)

    # Total Votes 
    for row in csvreader:
        candidate = row[2]

        # make list of ballot IDs 
        ballots.append(row[0])

        # make list of candidates
        if candidate not in candidates:
            candidate = row[2]
            candidates.append(candidate)

            # add candidtate to dictionary and set initial vote count
            votes[candidate] = 0
            
        # update vote count for each candidate
        votes[candidate] +=1

    # make list of percentage of votes for each candidate
    for candidate in votes:
        vote_count = votes.get(candidate)
        vote_percent = round((vote_count/int(len(ballots)))*100,3)
        results.append(vote_percent)
        
        # make list of candidates + percent votes + votes/candidate
        final_results.append(f"{candidate}: {vote_percent:.3f}% ({vote_count:,})")

        # winner is the candidate with the most votes 
        if vote_count>last_count:
            winner = candidate

        # reset last count value 
        last_count = vote_count
  
 # print results
print("Election Results")
print("----------------------------------")
print("Total Votes: " + str(len(ballots)))
print("----------------------------------")
for x in range(len(final_results)):
    print(final_results[x])
print("----------------------------------")
print(winner)
print("----------------------------------")

# Export results to analysis folder
output_path = os.path.join('python-challenge','PyPoll','analysis','analyzed_election_data.txt')

with open (output_path,"w") as file:
    file.write("Election Results" + '\n')
    file.write("----------------------------------" + '\n')
    file.write("Total Votes: " + str(len(ballots)) + '\n')
    file.write("----------------------------------" + '\n')
    for x in range(len(final_results)):
        file.write(final_results[x] + '\n')
    file.write("----------------------------------" + '\n')
    file.write(winner + '\n')
    file.write("----------------------------------" + '\n')

file.close()