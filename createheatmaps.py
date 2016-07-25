import os
from jinja2 import Environment, FileSystemLoader
import sqlite3
import pandas as pd

# define database
db = ""

# connect to database
con = sqlite3.connect(db)

# get table pokemon
df = pd.read_sql_query("SELECT * from pokemon", con)

# close connection to database
con.close()

# get eoncountered pokemon_id's
found_pokemon = df.drop_duplicates(subset = "pokemon_id")

# sort pokemon_id ascending
found_pokemon_sorted = found_pokemon.sort_values(by = "pokemon_id")

found_pokemon_sortet_list = found_pokemon_sorted['pokemon_id'].values.tolist()

# create heatmaps (html-files) for eoncoutered pokemons 
for x in found_pokemon_sortet_list:
	
	pokeid = x
	
	df_pokeid = df[(df['pokemon_id'] == pokeid)]
	
	# get weight (times of spawns per pokemon and spawnpoint)
	df_pokeid['weight'] = df_pokeid.groupby('spawnpoint_id')['spawnpoint_id'].transform(len)
	
	# delete spawnpoint duplets (necesarry? )
	df_pokeid = df_pokeid.drop_duplicates(subset = "spawnpoint_id")
	
	# to list
	xyz = zip(df_pokeid.latitude, df_pokeid.longitude, df_pokeid.weight)
	
	# create html-files
	PATH = os.path.dirname(os.path.abspath(__file__))
	
	TEMPLATE_ENVIRONMENT = Environment(
		autoescape=False,
		loader=FileSystemLoader(os.path.join(PATH, 'templates')),
		trim_blocks=False)
	
	def render_template(template_filename, context):
		return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
	
	def create_maps_html():
		fname = "maps/map_" + str(pokeid) + ".html"
		LatLngWei = xyz
		context = {
 		'LatLngWei': LatLngWei,
		}
		#
		with open(fname, 'w') as f:
			html = render_template('maps.html', context)
			f.write(html)
	
	def main():
		create_maps_html()
			
	if __name__ == "__main__":
		main()
