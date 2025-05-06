# importing necessary libraries
import pandas as pd
import plotly.express as px

# loading gazeeteer data containing place names and coordinates
coordinates_path = "gazetteers/NER_gazetteer.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t")

# loading the TSV file containing regex frequency counts per place and month
counts_df = pd.read_csv("ner_counts.tsv", sep="\t")

# Filter for January 2024 only
counts_df = counts_df[counts_df['month'] == '2024-01']

# merging the two dataframes on the common column "asciiname"
merge_df = pd.merge(coordinates_df, counts_df, on="asciiname")

## create a static map using frequency (count) as color
fig = px.scatter_map(merge_df, lat="latitude", lon="longitude", 
                    hover_name="asciiname", color="count", 
                    color_continuous_scale=px.colors.sequential.YlOrRd,
                    title="NER-extracted Placenames Frequency (January 2024)")
fig.update_layout(map_style="carto-darkmatter-nolabels")

# further customize the map with geographic features
fig.update_geos(
    projection_type="natural earth",
    fitbounds="locations",
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showland=True, landcolor="Green",
    showocean=True, oceancolor="LightBlue",
    showlakes=False, lakecolor="Blue",
    showrivers=True, rivercolor="Blue",
    showcountries=False, countrycolor="Brown"
)

# Save the static version of the map as PNG image
fig.write_image("ner_map.png", scale=2)

# saves the interactive map as an HTML file
fig.write_html("ner_map.html")

# show the customized map 
fig.show()
