# ===== INSTRUCTIONS FOR USE =====
# This is a Python 3 script to append latitude and longitude columns to a csv
# containing a column of city names.
#
# (1) Create a csv file with a "city" column and name it "Cities.csv"
# (2) Make sure this file and the CSV file are in the same folder.
# (3) Run the script. If you want to do it on Command Prompt, use the command:
#           python geoScript.py Cities.csv
# (4) The output will add "geo" to the front of the file name.
#           e.g., Cities.csv will become geoCities.csv

import requests
import json
import pandas as pd

# Allows user to enter CSV file name in terminal (e.g., Cities.csv)
nameCSV = input("What is your file name?\n")
api_key = input("Enter your API key to continue.\n")

# Function that calls the Google Maps API to generate a geoloction
def geoGoogle(geo, api_key):
    payload = {'address': geo, 'key': api_key}
    geoLocation = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params = payload)
    rLocation = geoLocation.json()
    try:
        latitude = rLocation['results'][0]['geometry']['location']['lat']
        longitude = rLocation['results'][0]['geometry']['location']['lng']
    except IndexError:
        latitude, longitude = None, None

    return latitude, longitude

# Parses CSV file into a DataFrame
df = pd.read_csv(nameCSV)

# Generate an empty list
slist = []

for i,_ in enumerate(df.index):
    s = df.at[i, 'city']    # name of column with geo that needs location
    slist.append(s)

latList, lonList = [], []

for city in slist:
    latitude, longitude = geoGoogle(city, api_key)[0], geoGoogle(city, api_key)[1]
    # print("Latitude and Longitude of {} is ".format(city), latitude, " ", longitude)
    latList.append(latitude)
    lonList.append(longitude)

# Creates two new columns in df to populate extracted latitude and longitude data
df["Latitude"], df["Longitude"] = pd.Series(latList), pd.Series(lonList)

# Exports final dataset into a CSV file
df.to_csv('geo' + nameCSV, sep = ';', index = False, decimal = '.', float_format = '%.3f')

# Notifies user of completed script.
print("We have added geolocation to your data. It is saved as geo" + nameCSV)
