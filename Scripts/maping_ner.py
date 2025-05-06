#import required libraries. 
import pandas as pd  #Our smart helper that reads and organizes data like a librarian
import plotly.express as px  #This one draws beautiful maps and graphs for us!
import kaleido  #USed to take a screenshot (PNG) of our map

#Let's open our treasure map. the file that tells us where places are on Earth.
coordinates_path = "C:/Users/LENOVO/Downloads/FASDH25-portfolio2/Data Outputs/NER_gazetteer.tsv"
places_df = pd.read_csv(coordinates_path, sep="\t")  # \t means the file is separated by tabs!

#Now open our box of mentions –it tells how many times each place was talked about.
counts_path = "C:/Users/LENOVO/Downloads/FASDH25-portfolio2/Data Outputs/ner_counts.tsv"
ner_df = pd.read_csv(counts_path, sep="\t")

#Making sure all our labels (column names) are in lowercase. this is because it will not create any issue later on for the case.
places_df.columns = places_df.columns.str.lower()
ner_df.columns = ner_df.columns.str.lower()

#If there's a date column, we will only focus on clumns from January 2024
if 'date' in ner_df.columns:
    ner_df['date'] = pd.to_datetime(ner_df['date'], errors='coerce')  #Turn messy dates into proper ones!
    ner_df['month'] = ner_df['date'].dt.to_period('M')  #Extract just the month part like "2024-01"
    jan_2024_df = ner_df[ner_df['month'] == "2024-01"]  #Keep only January stuff
else:
    jan_2024_df = ner_df  #If no date, assume it's all what we want

#combine places with their counts using the 'place' name.
merged_df = pd.merge(places_df, jan_2024_df, on="place")

#Turn the latitude and longitude into real numbers so we can actually place them on a map.
merged_df['latitude'] = pd.to_numeric(merged_df['latitude'], errors='coerce')
merged_df['longitude'] = pd.to_numeric(merged_df['longitude'], errors='coerce')
merged_df = merged_df.dropna(subset=['latitude', 'longitude'])  # We don’t want floating castles (missing locations)!

#draw an interactive magic map! The more a place was mentioned, the bigger it glows.
fig = px.scatter_geo(
    merged_df,
    lat="latitude",
    lon="longitude",
    size="count",  #Bigger circle = more mentions
    hover_name="place",  #When you hover, it tells the name
    color="count",  #Color shows intensity like a heatmap
    color_continuous_scale=px.colors.sequential.Plasma,  #Pretty colors like a rainbow sunset
    projection="natural earth"  #Flat, Earthy map (no spinning globe for now!)
)

#Let's give our map a cool look with oceans, rivers, and lands
fig.update_layout(
    title="Places Mentioned in January 2024",
    title_font_size=20,
    geo=dict(
        showland=True,
        landcolor="lightgray",  #Land in gentle gray
        showocean=True,
        oceancolor="lightblue",  #Water in lovely blue 
        showrivers=True,
        rivercolor="deepskyblue"  #Rivers dancing through the land
    )
)

#Show the magical, interactive map!
fig.show()

#Save this interactive wonder as an HTML file – you can open it in a browser anytime!
fig.write_html("ner_map.html")

#Now let’s make a picture version – a still photo of our lovely map
fig_static = px.scatter_geo(
    merged_df,
    lat="latitude",
    lon="longitude",
    hover_name="place",
    color="count",
    color_continuous_scale=px.colors.sequential.Plasma,
    projection="natural earth"
)

#Make the map prettier with green lands and fancy coastlines – like a fantasy storybook map
fig_static.update_geos(
    fitbounds="locations",
    showcoastlines=True,
    coastlinecolor="DarkRed",  #Red shores for drama
    showland=True,
    landcolor="DarkGreen",  #Forest-green lands 
    showocean=True,
    oceancolor="LightSeaGreen",  #Aqua oceans
    showrivers=True,
    rivercolor="RoyalBlue"  #Royal rivers flowing everywhere
)

fig_static.update_layout(
    title="Static NER Map — January 2024",
    title_font_size=18
)

#Peek at the static map before saving
fig_static.show()

#Capture the map like taking a polaroid – and save it as a PNG image!
fig_static.write_image("ner_map.png")# Download it in image form

