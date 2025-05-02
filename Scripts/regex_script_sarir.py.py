#This is from where I am starting the 2A exercies.

#Import all necessary libraries: 

import re
import os
import pandas as pd

#define a function which concerts a dictionary into a tsv file: Help taken from exeecises 10.1, class works.

def write_tsv(data, column_list, path):
    """This function converts a dictionary to a tsv file.

    It takes three arguments:
        data (dict): the dictionary
        column_list (list): a list of column names
        path (str): the path to which the tsv file will be written
    """
    
    # turn the dictionary into a list of (key, value) tuples (this is correct):
    items = list(data.items())
    # create a dataframe from the items list (this is correct):
    df = pd.DataFrame.from_records(items, columns=column_list)
    # write the dataframe to tsv:
    df.to_csv(path, sep="\t", index=False)



# define which folder to use:
# NB: these are different articles than in the previous weeks
folder = "articles"  

# define the patterns we want to search:

# load the gazetteer from the tsv file:
path = "gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

# build a dictionary of patterns from the place names in not just the first column, but look in the 2nd and 3rd as well:
patterns = {}
rows = data.split("\n")
print(rows)
for row in rows[1:]:
    columns = row.split("\t")
    name = columns[0]
    patterns[name] = 0

# count the number of times each pattern is found in the entire folder:
for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    #print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        # add the number of times it was found to the total frequency:
        patterns[pattern] += n_matches

# print the frequency of each pattern:
for pattern in patterns:
    count = patterns[pattern]
    if count >= 1:
        print(f"found {pattern} {count} times")

# call the function to write your tsv file:
columns = ["asciiname", "frequency"]
tsv_filename = "frequencies.tsv"
write_tsv(patterns, columns, tsv_filename)
