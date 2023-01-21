""" made by luna, 12.09.21, from 'The Python Mega Course' """

# folium uses python and translates it to html/css/javascript for the browser
import folium as f
# from jinja2.environment import get_spontaneous_environment
import pandas

#create a map using folium, using lattitude and longitude coords, the tile changes the map type
volc_map = f.Map(location=[42,-110], tiles="Stamen Terrain", zoom_start=5)

#load relevant data
data = pandas.read_csv("megapy/1webmap/volcanoes.txt")
lat = list(data["LAT"])
long = list(data["LON"])
elev = list(data["ELEV"])

#icons that change colour
def colour_icon(elevation):
    """ Assigns a colour to each map point based on elevation """
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation < 2500:
        return "orange"
    else:
        return "red"

# Create feature groups for each layer
fg_v = f.FeatureGroup(name="Volcanoes")
fg_p = f.FeatureGroup(name="Population")

# Add multiple markers for volcanoes
for lt, ln, el in zip(lat, long, elev):
    fg_v.add_child(f.Marker(location=[lt,ln],
    popup="Volcano at elevation %s" %el + ", with coordinates "+str(lt)+", "+str(ln),
    icon=f.Icon(color=colour_icon(el))))

# For population
fg_p.add_child(f.GeoJson(data=open("megapy/1webmap/world.json","r", encoding="utf-8-sig").read(),
style_function = lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"]< 10000000 else "orange" if 10000000<= x["properties"]["POP2005"] < 20000000 else "red"}))

volc_map.add_child(fg_p)
volc_map.add_child(fg_v)
volc_map.add_child(f.LayerControl())

#convert to html
volc_map.save("megapy/1webmap/map.html")
