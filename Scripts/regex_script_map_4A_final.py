
#import required libraries
import pandas as pd
import plotly.express as px

#Read the regex_counts.tsv file, which was the output of 2A (regex_counts.tsv)
df = pd.read_csv("C:/Users/LENOVO/Downloads/FASDH25-portfolio2/Data Outputs/regex_counts.tsv", sep="\t")
print(df.head()) #to see if I am on the right track.

#Get unique city names (place names in the input)
cities = df["placename"].unique()

#Print them one by one
print("Cities found in your output:")
for city in cities:
    print(city)

# Sample coordinates for some places (add more if needed)
place_coords = {
    "Gaza City": {"lat": 31.5010, "lon": 34.4668},
    "Jabalia": {"lat": 31.5386, "lon": 34.4989},
    "Bayt Lahya": {"lat": 31.5517, "lon": 34.5083}
}

# Add lat and lon columns to the dataframe
df["lat"] = df["placename"].map(lambda x: place_coords.get(x, {}).get("lat"))
df["lon"] = df["placename"].map(lambda x: place_coords.get(x, {}).get("lon"))

# Now we build the map!
# Each dot on the map shows a place where something was mentioned.
# Bigger and darker dots mean higher frequency.
# The map will animate month by month.
fig = px.scatter_geo(
    df,
    lat="lat",
    lon="lon",
    color="count",          # Color shows how many times the place was mentioned
    size="count",           # Size of the dot also shows frequency
    hover_name="placename", # When we hover on a dot, show the place name
    animation_frame="month",# Animation changes month by month
    title="Place Name Mentions Over Time",
    projection="natural earth"  # This is the style of the world map
)

# Save the interactive version (clickable and zoomable) as an HTML file
fig.write_html("regex_map.html")

# Save a still image version (like a screenshot) as a PNG file
fig.write_image("regex_map.png")

print("Maps have been saved successfully!")
