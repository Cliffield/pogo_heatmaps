# pogo_heatmaps
creates heatmaps from PogemonGo-Map

1. Set path of sqlite database in createheatmaps.py:	<br>
		db = "EXAMPLE.db"	<br>

2. Set latitute and longitude for startpoint of map in templates/map.html	<br>
		function initMap(){	<br>
		map = new google.maps.Map(document.getElementById('map'),	{<br>
		zoom: 13,	<br>
		center: {lat: 25.200254, lng: 4.100210 }, <-- change 25.200254 and 4.100210 to your point of interest	<br>
		mapTypeId: google.maps.MapTypeId.MAP	<br>

3. Set Google Maps API in tempates/map.html ( 4th last line)<br>
  
