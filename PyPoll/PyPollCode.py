import csv
file_path = 'Resources/election_data.csv'


def analyze_vote_data(file_path):
    # Initialize variables
    total_votes = 0
    candidates = {}
    winner = ""
    max_votes = 0

    # Read the CSV file
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        # Go through each row in the CSV file
        for row in reader:
            # Extract data from the row
            voter_id = row[0]
            county = row[1]
            candidate = row[2]

            # Count the total number of votes
            total_votes += 1

            # Count the votes for each candidate
            if candidate in candidates:
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1

    # Determine the winner out of the candidates
    for candidate, votes in candidates.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # Calculate the percentage of votes each candidate won
    percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

    # Print out the analysis results to the terminal
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        percentage = percentages[candidate]
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # Put the analysis results to a text file
    output_file = "election_results.txt"
    with open(output_file, 'w') as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            percentage = percentages[candidate]
            file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {winner}\n")
        file.write("-------------------------\n")

# Text File Output
file_path = 'election_data.csv'
analyze_vote_data(file_path)
output_file = "election_results.txt"
    