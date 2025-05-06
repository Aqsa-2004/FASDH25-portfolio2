# FASDH25-portfolio2
### Group members: Aqsa Anwerali, Sarir Ahmed and Kamran Abid.
## Folder Structure:
We have structured our folder in a unique way to make it easy for us: 
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
### Code Structure: (AI helped me made this flow)
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
### Overview: 
this part focuses on extracting place names from news articles published in January 2024, using Stanza's NER (Named Entity Recognition) model.
### NLP Environment Setup: 
This code was done in google colab that's why it varies from other codes of this mini project.
1. Library Installation:
   - Installed the `stanza` Python library.
   - Downloaded the English language model using `stanza.download('en')`.
2. Pipeline Configuration:
   - Initialized a Stanza NLP pipeline for English text with the NER processor enabled.
   - This pipeline allows Stanza to recognize named entities — specifically location names — in the text.
### Corpus Preparation
1. Repository Cloning:
   - Cloned the GitHub repository: `FASDH25-portfolio2`, which contains the full text corpus (documents and all required articles).
2. Directory Linking:
   - Defined the file path to the directory containing the articles, allowing the script to access and process the documents directly.
3. Temporal Filtering:
   - Applied a filter to process only files starting with `2024-01`, targeting articles published in January 2024 specifically.
### OutPut:
The output was place names and counts as give bellow:
place	count
Israel	5567
Gaza	5565
Palestine	427
United States	557
Welch	4
...

## 3: Geocoding Place Names
### Overview: 
In this project, we have extracted place names mentioned in January 2024 and mapped them using Natural Language Processing (NLP) method. We have evaluated the accuracy of two methods to recognize geographical entities; Named Entity Recognition (NER) using Stanza and Regex with a gazetteer.
### Input Data:
- Used `ner_counts.tsv`  
  This file contains place names identified in the earlier NLP phase (2B) using the Stanza library.
### Code Process:
1. Libraries Used:
   - `requests` – to send HTTP requests to the GeoNames API
   - `time` – to introduce delays between API calls and avoid rate-limiting
2. Function Defined:
   - A custom Python function `get_coordinates()` was created to query the GeoNames REST API.
   - Parameters used:
     - `username=kamran.abid`
     - `fuzzy=0` – ensures more precise matches
     - `maxRows=1` – limits the number of returned results to one per query
3. Data Extraction:
   - The TSV file was read line by line, and unique place names were extracted into a list.
4. API Querying:
   - For each place name, the script queried the GeoNames API.
   - If a result was found, the latitude and longitude were recorded.
   - If not found (due to spelling or missing data), `"NA"` was assigned for both coordinates.
   - The data with "NA" in front of the names, were checked and added manually on excell and then the output saved.
5. Result Structuring:
   - All retrieved data was organized into a list of dictionaries:
     ```json
     [{"Place": "Lahore", "Latitude": "31.5497", "Longitude": "74.3436"}, ...]
     ```
6. Output File:
   - `NER_gazetteer.tsv` was created containing three columns:
     

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
