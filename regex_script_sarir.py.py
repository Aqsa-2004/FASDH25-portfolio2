#Imprt necessary libraries:
#For pattern matching using regular expressions
import re
#To interact with the file system (e.g., read files from folders) 
import os
#To work with tabular data and export to .tsv format
import pandas as pd

#This function saves data (a list of rows) to a .tsv file using pandas: Help taken from exeecises 10.1, class works.

def write_tsv(rows, column_list, path):

     #create a DataFrame from the data
    df = pd.DataFrame(rows, columns=column_list)
    
    # save it as a .tsv file (tab-separated)
    df.to_csv(path, sep="\t", index=False)


# Defining the folder where the articles are present
# This is the folder containing the text articles we want to analyze 
folder = "articles"  

# Load the list of place names (gazetteer) from a TSV file: Help taken from exeecises 10.1, class works 
path = "gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

# This function helps build a flexible regular expression for each place name
def flexible_regex(name):
    # Create variations to catch alternate spellings and transliterations: Help taken with Chat GPT, Solution 1
    name = re.sub(r"Kh", r"(Kh|K|Ḫ)", name, flags=re.IGNORECASE)
    name = re.sub(r"a", "[aā]", name, flags=re.IGNORECASE)
    name = re.sub(r"i", "[ie]", name, flags=re.IGNORECASE)
    name = re.sub(r"[uo]", "[ouū]*", name, flags=re.IGNORECASE)
    name = name.replace(" ", r"\s?")
    return name

# Dictionary to store regex patterns for each place
# A dictionary of patterns from the place names in not just the first column, but look in the 2nd and 3rd as well:
patterns = {}
# Split the gazetteer into rows (one row per place)
rows = data.split("\n")

#Skip the first row (header) and process each place
for row in rows[1:]:
    columns = row.split("\t") # each column in tsv is separated by tabs to make them more easier
    asciiname = columns[0] #first column has name for the place


    #Skip rows that don't have at least 6 columns and others may beb incomplete    
    if len(columns) < 6:
        continue # skip if the row is incompletee

    #Initialize the list with the place name
    name_variants = [asciiname]  # start with the main name


    # Get the alternate names from the 6th column which is counted as 5, if present
    alternate_names = columns[5].strip()

    
    if alternate_names:
        # Split the alternate names by comma and get a list of name variants
        alternate_list =alternate_names.split(",") # split by commas

        #Loop through each alternate name in the list
        for alternate in alternate_list:
            #remove any whitspace from the alternate name
            alternate = alternate.strip()
            # add the alternate name to the list if present 
            if alternate:
                name_variants.append(alternate)  # add valid alternates

    #apply flexible matching to all name variants
    new_variants = []
    for name in name_variants:
        result = flexible_regex(name)
        new_variants.append(result)
    name_variants = new_variants

    #Building a single regex pattern that matches any variant (using '|' for alternation) - Help from ChatGPT - Conversation 5 (writing regex pattern)
    #the | is used to get the alternation as it means or
    #re.escape() is used to escape any special characters in the place name
    regex_pattern = "|".join(name_variants)
    # it includes all the names and their variants with their number
    patterns[asciiname] = {"pattern": regex_pattern, "count":0}

    


# this dictionary stores how many times each place name was mentioned per month 
mentions_per_month = {}


#Set the starting date of the war in Gaza to filter articles - Help from ChatGPT - Conversation 2 and 4(removal of datetime)
war_start_date = "2023-10-07"

for filename in os.listdir(folder):
    # Extract the date from the filename(as the format is YYYY-MM-DD_)
    date_str = filename.split("_")[0]

    #Skip the file if it is before the start of  the war
    if date_str < war_start_date:
        continue
    
    

# build the file path to the current articles:
    file_path = os.path.join(folder, filename)        

    #Open and read the articles 
    with open(file_path, encoding="utf-8") as file:
        text = file.read()
        

    # Loop through each place to search for matches in the text
    for place in patterns:
        pattern = patterns[place]["pattern"] # Get regex-safe pattern 
        matches = re.findall(pattern, text, re.IGNORECASE)
        count = len(matches) # number of times the place was found
        
        # add the number of times the place was found to the total frequency:
        patterns[place]["count"] += count
        
        # extract the month from the date string
        month_str = date_str[:7]
        

        # initialize place and month in mentions_per_month dictionary if not done already
        if place not in mentions_per_month:
            # empty dictionary if place is not found
            mentions_per_month[place] = {}
        #check if the month is not in the dictionary 
        if month_str not in mentions_per_month[place]:
            # if month is not found, place the month count to 0
            mentions_per_month[place][month_str] = 0

        #Add the new matches on the place names to the number of times it was mentioned that month     
        mentions_per_month[place][month_str] += count
          


# print the final dictionary showing how often each place was mentioned by month
# Loop through each place in the mentions_per-month dictionary
for place in mentions_per_month:
    # Start a dictionary like printout for the current place 
    print(f'"{place}": {{')

    #Get a list of all the months in which the place names are mentioned 
    month_list = list(mentions_per_month[place].keys())

    #loop through each month to print the corresponding mention count
    for month in month_list:
        count = mentions_per_month[place][month] #  get the count for that month

        # display the output with a comma except for the last item to keep it clean 
        if month != month_list[-1]:
            print(f'    "{month}": {count},')
        else:
            print(f'    "{month}": {count}')

    # close the dictionary block and print the output
    print("},")

#Convert the mentions_per_month dictionary to list of rows for output
rows = []

#loop through each place again to prepare structured data for export 
for place in mentions_per_month:

    # loop through each month and find the number of times the place is mentioned 
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]

        #Append a tuple (place, month, count) to the rows list
        rows.append((place, month, count))

#Write final result to tsv file for external use        
write_tsv(rows, ["placename","month", "count"], "regex_counts.tsv")

