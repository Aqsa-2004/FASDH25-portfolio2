# FASDH25-portfolio2
### Group members: Aqsa Anwerali, Sarir Ahmed and Kamran Abid.
## Folder Structure:
- GAZA_NER_Aqsa_Sarir_Kamran
- regex_script_sarir_aqsa_kamran.ipynb  
- articles
- gazetteer.txt      
- ner_counts.tsv    
- regex_counts.tsv  
- maps    
- map_ner_jan2024.png
- map_regex_jan2024.png

## 2A: Place Name Counter using Regex
It focuses on identifying and counting how often specific place names (mainly from Gaza) appear in a collection of news articles. We use regular expressions (regex) to find flexible matches for place names — allowing for different spellings and variations.
### Objectives:
- To apply regex patterns for identifying place names in text.
- To track how often these names appear in articles after the Gaza war began on October 7, 2023.
- To output the results in a tab-separated values (TSV) file for further analysis.
### Tools and Libraries:
- Python
- `re` (for regex)
- `os` (for file handling)
- `pandas` (for tabular data and TSV export)
### Code Structure:
project_2a/
│
├── articles/ # Folder with article text files
├── gazetteers/
│ └── geonames_gaza_selection.tsv # File with place names and their alternate spellings
├── regex_counter.py # Main script for the project
└── regex_counts.tsv # Output file with monthly counts
### Output:
placename     month     count
Gaza          2023-10   34
Rafah         2023-11   18
Khan Younis   2023-12   22
...



## 2B. Use stanza to extract all place names from (part of) the corpus
This part uses Stanza's Named Entity Recognition (NER) model to extract place names from articles published in January 2024. 

- First, we set up the NLP environmnet for which we installed the stanza library and downloaded the English language model for it. Then to enable entity recognition on English text, we created a processing pathway and this established the basis for recognizing place names in our corpus. 
- After that to link up with the corpus, we cloned the FASDH25-portfolio2 GitHub repository that contained all the documents and articles we needed. To make it easier for the script to find these articles we specified the directory pathway in which they were stored.
- Furthermore, we restricted the corpus to process only files that began with 2024-01 which made it possible to target articles from January 2024 specifically.

## 3: Analyze and Visualize place names found in articles about the Gaza war.
In this project, we have extracted place names mentioned in January 2024 and mapped them using Natural Language Processing (NLP) method. We have evaluated the accuracy of two methods to recognize geographical entities; Named Entity Recognition (NER) using Stanza and Regex with a gazetteer.

## 4A: Plotting Places Mentioned, Mapping – Gaza War
### Overview:
This project visualizes how often different place names were mentioned in a collection of articles about the Gaza war, using geographic coordinates and an animated map. It builds upon the output from 2A (regex_counts.tsv) and maps these mentions over time using Plotly.
### File used:
- regex_counts.tsv: Output from 2A, contains place names, months, and count of mentions.
- geonames_gaza_selection.tsv: A gazetteer with location names and coordinates
### Flow of the code:
- Imports libraries like pandas and plotly.
- Reads the mention data from regex_counts.tsv.
- Loads the gazetteer file to get place coordinates.
- Merges both files using the placename and name columns to attach coordinates to the mention data.
- Prints previews to check if merging worked and what cities were included.
- Creates a geographic map using Plotly that animates month by month.
- Saves the outputs
### Output: 
- An interactive globe-style map that shows which places were mentioned each month.
- A still snapshot version of the map for reports or presentations.
### Note: 
1. Before running this code, make sure regex_counts.tsv and geonames_gaza_selection.tsv are in the correct folders.
2. Run the script in Python because it is written according to it, not google colab. 
3. Check the data Output for regex_map.html and regex_map.png.
             
## 4B: 
