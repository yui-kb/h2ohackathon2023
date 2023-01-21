

# folium uses python and translates it to html/css/javascript for the browser
import folium as f
# from jinja2.environment import get_spontaneous_environment
import pandas


#load relevant data
data = pandas.read_csv("data/Sensors_pipes_data.csv")
start_lat = list(data["Start.Latitude"])
start_long = list(data["Start.Longitude"])
end_lat = list(data["End.Latitude"])
end_long = list(data["End.Longitude"])
#prob_of_leak = list(data["prob.of.leak"])
#likelihood = list(data["Likelihood"])
likelihood = ["Low", "Medium", "High"]*len(start_long)
colours=[]

#create a map using folium, using lattitude and longitude coords, the tile changes the map type
volc_map = f.Map(location=[start_lat[0],start_long[0]], tiles="Stamen Terrain", zoom_start=13)


#icons that change colour
def colour_icon(likelihood):
    """ Assigns a colour to each map point based on likelihood of leak """
    if likelihood == "Low":
        return "green"
    elif likelihood == "Medium":
        return "orange"
    else:
        return "red"

# Create feature groups for each layer
fg_v = f.FeatureGroup(name="Sensors")
fg_p = f.FeatureGroup(name="Population")

# Add multiple markers for volcanoes
for lt, ln, li in zip(start_lat, start_long, likelihood):
    fg_v.add_child(f.Marker(location=[lt,ln],
    popup="Sensor with coordinates "+str(lt)+", "+str(ln),
    icon=f.Icon(color="black")))
    colours += [colour_icon(li)]

# For population
fg_p.add_child(f.GeoJson(data=open("map/world.json","r", encoding="utf-8-sig").read()))
#style_function = lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"]< 10000000 else "orange" if 10000000<= x["properties"]["POP2005"] < 20000000 else "red"}))

volc_map.add_child(fg_p)
volc_map.add_child(fg_v)
volc_map.add_child(f.LayerControl())

#Plot lines with colours based off risk to burst
points = (list(zip(start_lat, start_long)), list(zip(end_lat,end_long)))
for i, point in enumerate(points): 
    f.PolyLine(point, color=colours[i], weight=2.5, opacity=1).add_to(volc_map)

#convert to html
volc_map.save("map/map.html")
