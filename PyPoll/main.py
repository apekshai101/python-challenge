import os
import csv

# Create path for your file
electioncsv = os.path.join('/Users/apekshaingole/Desktop/python-challenge/PyPoll/Resources/election_data.csv')

# Open and Read the CSV file
with open(electioncsv) as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Skip the header row
    csvheader = next(csvfile)
    
      # Initialize variables 
    total_votes = 0
    candidates = []
    names = []
    votes = []

    # Iterate through each row in the CSV file
    for row in csvreader:
        # Count the total number of votes by incrementing total votes for each row
        total_votes += 1

        # Extract the name of candidate from the current row & third column(index2)
        i = row[2]

        # Update the vote count in the candidates list.If the candidate is in the list, it increments the count.
        # If not,adds the new candidate to the list names & starts the vote count at 1 for that candidate
        if i in candidates:
            votes[candidates.index(i)] += 1
        else:
            candidates.append(i)
            names.append(i)
            votes.append(1)

        # if the current candidate has more votes than the leading candicate in names list,update name of winner
        if votes[candidates.index(i)] > votes[candidates.index(names[0])]:
            names[0] = i

# Calculate the percentage of votes each candidate won
    candidates_percentage = []
    for v in votes:
        percentage = (v / total_votes) * 100
        candidates_percentage.append(percentage)
   
# Print the results to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for j in range(len(candidates)):
    print(f"{candidates[j]}: {candidates_percentage[j]:.3f}% ({votes[j]})")

print("-------------------------")
print(f"Winner: {names[0]}")
print("-------------------------")

# Export Results to a Text File
outputfile = os.path.join("Analysis","analysis.txt")
with open(outputfile,"w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")    
    for j in range(len(candidates)):
        txtfile.write(f"{candidates[j]}: {candidates_percentage[j]:.3f}% ({votes[j]})\n")        
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {names[0]}\n")
    txtfile.write("-------------------------\n")
        
    
