# FASDH25-portfolio2
### Group members: Aqsa Anwerali, Sarir Ahmed and Kamran Abid.
## Analyze and Visualize place names found in articles about the Gaza war.
In this project, we have extracted place names mentioned in January 2024 and mapped them using Natural Language Processing (NLP) method. We have evaluated the accuracy of two methods to recognize geographical entities; Named Entity Recognition (NER) using Stanza and Regex with a gazetteer.
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


## 2B. Use stanza to extract all place names from (part of) the corpus
This part uses Stanza's Named Entity Recognition (NER) model to extract place names from articles published in January 2024. 

- First, we set up the NLP environmnet for which we installed the stanza library and downloaded the English language model for it. Then to enable entity recognition on English text, we created a processing pathway and this established the basis for recognizing place names in our corpus. 
- After that to link up with the corpus, we cloned the FASDH25-portfolio2 GitHub repository that contained all the documents and articles we needed. To make it easier for the script to find these articles we specified the directory pathway in which they were stored.
- Furthermore, we restricted the corpus to process only files that began with 2024-01 which made it possible to target articles from January 2024 specifically.

             

