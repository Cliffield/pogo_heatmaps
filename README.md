# pogo_heatmaps
creates heatmaps from PogemonGo-Map

1. Define path of sqlite database in createheatmaps.py:
  # define database
  db = "EXAMPLE.db" 

2. Set latitute and longitude for startpoint of map in templates/map.html
  function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 13,
      center: {lat: 25.200254, lng: 4.100210 }, <-- change 25.200254 and 4.100210 to your point of interest
      mapTypeId: google.maps.MapTypeId.MAP
      
      
3. Set Google Maps API in tempates/map.html ( 4th last line)
  <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=INSERT-GOOGLE-MAPS-API-KEY-HERE&signed_in=true&libraries=visualization&callback=initMap">
  </script>
  
