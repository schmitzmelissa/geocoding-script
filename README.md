# geocoding-script
A script that converts a city and state to latitude and longitude coordinates using the Google Maps API.

**Example Geodata Plot in Tableau:** https://public.tableau.com/profile/melissa.schmitz#!/vizhome/SimpleScriptsHowcanIproducecleanmapdataforgeodatavisualizations/MapPlot

# Required Python Libraries
- Requests
- Pandas
- Google Maps (will need to generate your own API key)

# Instructions for Use
This is a Python 3 script to append latitude and longitude columns to a csv containing a column of city names.
1. Create a csv file with a "city" column and name it "Cities.csv"
2. Make sure this file and the CSV file are in the same folder.
3. Run the script. It will prompt you for your file name and API key.
4. The output will add "geo" to the front of the file name (e.g., Cities.csv will become geoCities.csv; not to be confused with the Yahoo! owned website, of course).
