
#import required libraries
import pandas as pd
import plotly.express as px

#Read the regex_counts.tsv file, which was the output of 2A (regex_counts.tsv)
counts_df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio2/Data Outputs/regex_counts.tsv", sep="\t")

#Loading the gazetteer.
gazetteer_df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio2/gazetteers/geonames_gaza_selection.tsv", sep="\t")

#print both of the documents to see the names of the column which needs to be merged.
print("Counts DF columns:", counts_df.columns.tolist()) 
print("Gazetteer DF columns:", gazetteer_df.columns.tolist())


#Merge based on the 'placename' column: Help taken from discussion forum and Chat GPT- solution 1
merged_df = pd.merge(counts_df, gazetteer_df, left_on="placename", right_on="name", how="left")


print(counts_df.head())  #To check the regex_counts file
print(merged_df.head())  #To check the merged file with coordinates


#To see by printing unique city names to verify what was matched
print("Cities found in your output:")
print(merged_df["placename"].unique())

#Now here I will build the map: Help taken from one of my friends and course 11.2
#The map will animate month by month.
fig = px.scatter_geo(
    merged_df,
    lat="latitude",  
    lon="longitude", 
    color="count",
    size="count",
    hover_name="placename",
    animation_frame="month",
    title="Place Name Mentions Over Time",
    projection="orthographic",  # 3D globe style
)

fig.update_geos(
    center=dict(lat=31.5, lon=34.5),  # Centered around Gaza
    projection_scale=6,              # Zoom level (higher = more zoomed in)
    showland=True, landcolor="LightGray",
)


#save the interactive version (clickable and zoomable) as an HTML file: Help taken from Chat GPT- solution 2
fig.write_html("regex_map.html")
#Save a still image version (like a screenshot) as a PNG file
fig.write_image("regex_map.png")

print("Maps have been saved successfully!") #to see if the code is running till the end
