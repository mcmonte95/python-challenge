import os
import csv



#get working directory path
cwd = os.getcwd()

#create path to budget_data.csv
csvpath = os.path.join(cwd, 'Resources', 'election_data.csv')

#Open the csv file
with open(csvpath, encoding='utf-8') as csvfile:
    
    
    csvreader = csv.reader(csvfile, delimiter=',')
   
    #Store the first row of the csv and then advance to the next row
    column_headers = next(csvreader)
   
    #Create empty lists for ballot ID, County, and Candidate name
    ID_list = []
    county_list = []
    candidate_list = []
   
    #read the elements from the csv into their respective lists
    for row in csvreader:
        ID_list.append(int(row[0]))
        county_list.append(str(row[1]))
        candidate_list.append(str(row[2]))
       
       

    #calculate total votes cast by the length of the ID_list
    total_votes = len(ID_list)
    
    #calculate total votes per candidate using list comprehension on the candidate list for each candidate
    charles_votes = len([element for element in candidate_list if element == "Charles Casper Stockham" ])
    diane_votes = len([element for element in candidate_list if element == "Diana DeGette" ])
    raymond_votes = len([element for element in candidate_list if element == "Raymon Anthony Doane" ])
     
    #create dictionary with candidate as the key and vote counts as the value
    vote_counts = {"Charles Casper Stockham" : charles_votes,
                             "Diana DeGette" : diane_votes,
                      "Raymon Anthony Doane" : raymond_votes} 
    
    
    # (1) find the key in the dictionary that has the highest value and make that candidate the winner
    winner = max(vote_counts, key=vote_counts.get)
       
#create a function that will both print and write to a file this way we dont have to repeat both the print and write statements       
def print_and_write(filename, string):
    filename.write(string + "\n")
    print(string)


output_path = os.path.join(cwd, 'analysis', 'Election_Results.txt' )


#write to a file and print results using the function created
# (2) calculate the % of votes gotten per candidate within the f strings and round to 3 decimal points
with open(output_path, 'w') as file:
    print_and_write(file, "Election Results\n")
    print_and_write(file, "----------------------------\n")
    print_and_write(file, f"Total Votes: {total_votes}\n")
    print_and_write(file, "----------------------------\n")
    print_and_write(file, f"Charles Casper Stockham: {round(((charles_votes/total_votes)*100),3)}% ({charles_votes})\n")
    print_and_write(file, f"Diana DeGette: {round(((diane_votes/total_votes)*100),3)}% ({diane_votes})\n")
    print_and_write(file, f"Raymon Anthony Doane: {round(((raymond_votes/total_votes)*100),3)}% ({raymond_votes})\n")
    print_and_write(file, "----------------------------\n")
    print_and_write(file, f"Winner: {winner}\n")
    print_and_write(file, "----------------------------\n")
    