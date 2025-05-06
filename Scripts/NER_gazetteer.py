#Import necessary libraries
import requests
import time

#using my user name of 
geonames_username = "kamran.abid"
#Define a function to get coordinates (latitude and longitude) for a place
def get_coordinates(place, username=geonames_username, fuzzy=0, timeout=1):
    """This function gets a single set of coordinates from the geonames API."""
    time.sleep(timeout)  #Wait to avoid overloading the server
    url = "http://api.geonames.org/searchJSON?"
    
    #Set up the parameters for the API request
    params = {"q": place, "username": username, "fuzzy": fuzzy, "maxRows": 1, "isNameRequired": True}

    #Send a request to the GeoNames API with the place name
    response = requests.get(url, params=params)

    #Convert the response into a Python dictionary
    results = response.json()

    try:
        #Try to get the first result from the API response and extract latitude and longitude
        result = results["geonames"][0]
        return {"latitude": result["lat"], "longitude": result["lng"]}
    except (IndexError, KeyError):
        #If there is no result or an error, return "NA" for both latitude and longitudes
        return {"latitude": "NA", "longitude": "NA"}  #Return "NA" if no coordinates found

#Make an empty list to store place names
place = []

#Open the TSV file that contains place names
with open("C:/Users/Hp/Downloads/FASDH25-portfolio2/Data Outputs/ner_counts.tsv", 'r', encoding="utf-8") as file:
    lines = file.readlines() #Read all lines from the file

#Get the first line and find out which column has the place names
header = lines[0].strip().split('\t')
place_index = header.index('place')

#Go through each line after the header and get the place names
for line in lines[1:]:
    columns = line.strip().split('\t')
    if len(columns) > place_index:
        place.append(columns[place_index]) #Add the place name to the list

#meke and empty list to store place names with their coordinates
coordinates_data = []

#For each place, get the coordinates and store them
for place_name in place:
    coordinates = get_coordinates(place_name) #Call the function to get latitude and longitude
    coordinates_data.append({'Place': place_name, 'Latitude': coordinates['latitude'], 'Longitude': coordinates['longitude']})

    #Print the place name with its coordinates
    print(f"{place_name}: {coordinates['latitude']}, {coordinates['longitude']}")

#Name of the output file where results will be saved
filename = "NER_gazetteer.tsv"

#Open a new TSV file to write the results
with open(filename, 'w', encoding="utf-8") as file:
    file.write('Place\tLatitude\tLongitude\n') #Write the header line
    
    #To Go through each place and write its name and coordinates to the file
    for row in coordinates_data:
        file.write(f"{row['Place']}\t{row['Latitude']}\t{row['Longitude']}\n")
#Print a message to see if the NER's are saved successfully
print("Coordinates written to NER_gazetteer.tsv")
