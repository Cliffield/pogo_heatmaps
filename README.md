# pogo_heatmaps

creates heatmaps from PokemonGo-Map gathered data<br>
It creates for every particular pokemon a heatmap in the subfolder "maps". The mapped spawnpoints are weightet by the count of spaws of the particular pokemon at this spawnpiont. The heatmaps are just html-files with coordinates and the weigth using google maps api for heatmaps.

<p>
Data import from sqlite and MySQL-Database possible
Just set configs at head of script.
</p>

'''
########################################################
## define settings here
########################################################
input_type = "sqlite" # "sqlite" or "MySQL"

# for sqlite
database = "pogom.db" # sqlite filename e.g. "pogom.db" 

# for MySQL
host="127.0.0.1" #host
user="dbuser" # user
password="foo" # password
db="bar" # database

output_folder = "maps" # output folder for maps e.g. "maps"

# startpoint of map; change to your poi
lat_start = "52.211184" # latitude
lng_start = "13.047870" # longitude

GoogleMapsKey = "insert_key_here" # GMAPS_API_KEY 

language = "en" # pokemon names in "en", "fr" or "de"
########################################################
'''  


![Alt text](/static/screenshot.png?raw=true "screenshot")


