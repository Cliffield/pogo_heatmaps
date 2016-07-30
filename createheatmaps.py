#!/usr/bin/python
#	# -*- coding: utf-8 -*-
import os
from jinja2 import Environment, FileSystemLoader
import sqlite3
#import MySQLdb #packet name is MySQL-python
import pymysql
import pandas as pd

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



PATH = os.path.dirname(os.path.abspath(__file__))
	
TEMPLATE_ENVIRONMENT = Environment(
	autoescape=False,
	loader=FileSystemLoader(os.path.join(PATH, "templates")),
	trim_blocks=False)

def render_template(template_filename, context):
	return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def create_maps_html():
	fname = output_folder + "/map_" + str(pokeid) + ".html"
	context = {
	"LatLngWei": LatLngWei,
      "lat_start":lat_start,
      "lng_start":lng_start,
      "GoogleMapsKey":GoogleMapsKey
	}
	with open(fname, "w") as f:
		html = render_template("map.html", context)
		f.write(html)

def main():
	create_maps_html()

def create_index():
	fname = "index.html"
	context = {
	"pokeid": pokeid,
	"found_pokemon_id":found_pokemon_id,
	"name":name,
	"spawns":spawns
	}
	with open(fname, "w") as f:
		html = render_template("index.html", context)
		f.write(html)

if input_type.lower() == "sqlite":
    con = sqlite3.connect(database)
elif input_type.lower() == "mysql":
    con = pymysql.connect(
	host=host,
	user=user,
        password=password,
	db=db
        )
else:
	print "Type of database not specified."

# get table pokemon from database
df = pd.read_sql_query("SELECT * from pokemon", con)

# close connection to database
con.close()

# sort pokemon_id ascending and get every pokemon_id only once in the array
found_pokemon_id = df.pokemon_id.sort_values().unique()

# pokemon names encoding
name = pd.read_json("static/locales/pokemon." + language + ".json", typ = "series")

# spawns per pokemon
spawns = pd.value_counts(df["pokemon_id"])

# test if folder maps exist, else create it
try: 
    os.makedirs(output_folder)
except OSError:
    if not os.path.isdir(output_folder):
        raise

# create heatmaps (html-files) for eoncontered pokemons 
for pokeid in found_pokemon_id:

	df_pokeid = df[(df["pokemon_id"] == pokeid)]
		
	# get weight (times of spawns per pokemon and spawnpoint)
	weight = df_pokeid.groupby("spawnpoint_id")["spawnpoint_id"].transform(len)
	
	# delete spawnpoint duplets
	df_pokeid = df_pokeid.drop_duplicates(subset = "spawnpoint_id")
	
	# to list
	LatLngWei = zip(df_pokeid.latitude, df_pokeid.longitude, weight)
	
	# create html-files
				
	if __name__ == "__main__":
		main()
		
create_index()
