

""" made by luna, 12.09.21, from 'The Python Mega Course' """

# folium uses python and translates it to html/css/javascript for the browser
import folium as f
# from jinja2.environment import get_spontaneous_environment
import pandas

def create_map(start_lats, start_longs, end_lats, end_longs, colours):
    #load relevant data
    '''data = pandas.read_csv("data/Sensors_pipes_data.csv")
    start_lat = list(data["Start.Latitude"])
    start_long = list(data["Start.Longitude"])
    end_lat = list(data["End.Latitude"])
    end_long = list(data["End.Longitude"])'''
    
    #prob_of_leak = list(data["prob.of.leak"])
    #likelihood = list(data["Likelihood"])
    #likelihood = ["Low", "Medium", "High"]*len(start_long)
    #colours=[]

    #create a map using folium, using lattitude and longitude coords, the tile changes the map type
    volc_map = f.Map(location=[start_lats[0],start_longs[0]], tiles="Stamen Terrain", zoom_start=13)


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
    for lt, ln in zip(start_lats, start_longs):
        fg_v.add_child(f.Marker(location=[lt,ln],
        popup="Sensor with coordinates "+str(lt)+", "+str(ln),
        icon=f.Icon(color="black")))
        #colours += [colour_icon(li)]

    # For population
    fg_p.add_child(f.GeoJson(data=open("map/world.json","r", encoding="utf-8-sig").read()))
    #style_function = lambda x: {"fillColor": "yellow" if x["properties"]["POP2005"]< 10000000 else "orange" if 10000000<= x["properties"]["POP2005"] < 20000000 else "red"}))

    volc_map.add_child(fg_p)
    volc_map.add_child(fg_v)
    volc_map.add_child(f.LayerControl())

    #Plot lines with colours based off risk to burst
    #print(start_lats)
    points = (list(zip(start_lats, start_longs)), list(zip(end_lats,end_longs)))
    print(points)
    for i, point in enumerate(points): 
        print(colours[i])
        f.PolyLine(point, color=colours[i], weight=2.5, opacity=1).add_to(volc_map)

    #convert to html
    volc_map.save("map/map.html")
