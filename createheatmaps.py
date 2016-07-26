import os
from jinja2 import Environment, FileSystemLoader
import sqlite3
import pandas as pd

# define output folder
output_folder = "maps"

# define database
database = ""

# connect to database
con = sqlite3.connect(database)

# get table pokemon
df = pd.read_sql_query("SELECT * from pokemon", con)

# close connection to database
con.close()

# sort pokemon_id ascending and get every pokemon_id only once in the array
found_pokemon_id = df[("pokemon_id")].sort_values().unique()

# test if folder maps exist, else create it
try: 
    os.makedirs(output_folder)
except OSError:
    if not os.path.isdir(output_folder):
        raise

# create heatmaps (html-files) for eoncoutered pokemons 
for x in found_pokemon_id:
	
	pokeid = x
	
	df_pokeid = df[(df["pokemon_id"] == pokeid)]
	
	# get weight (times of spawns per pokemon and spawnpoint)
	weight = df_pokeid.groupby("spawnpoint_id")["spawnpoint_id"].transform(len)
	
	# delete spawnpoint duplets
	df_pokeid = df_pokeid.drop_duplicates(subset = "spawnpoint_id")
	
	# to list
	LatLngWei = zip(df_pokeid.latitude, df_pokeid.longitude, weight)
	
	# create html-files
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
		}
		with open(fname, "w") as f:
			html = render_template("maps.html", context)
			f.write(html)
	
	def main():
		create_maps_html()
			
	if __name__ == "__main__":
		main()
