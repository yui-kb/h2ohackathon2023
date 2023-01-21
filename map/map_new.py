""" Core code for creating prediction plot. """

# External imports
# Folium uses python and translates it to html/css/javascript for the browser
import folium as f

def create_map(start_lats, start_longs, end_lats, end_longs, colours):

    #Create a map using folium, using lattitude and longitude coords, the tile changes the map type
    pipe_map = f.Map(location=[start_lats[0],start_longs[0]], tiles="Stamen Terrain", zoom_start=13)

    # Create feature groups for each layer
    fg_v = f.FeatureGroup(name="Sensors")
    fg_p = f.FeatureGroup(name="Population")

    # Add multiple markers for volcanoes
    for lt, ln in zip(start_lats, start_longs):
        fg_v.add_child(f.Marker(location=[lt,ln],
        popup="Sensor with coordinates "+str(lt)+", "+str(ln),
        icon=f.Icon(color="black")))
        #colours += [colour_icon(li)]

    #Add base map and points
    fg_p.add_child(f.GeoJson(data=open("map/world.json","r", encoding="utf-8-sig").read()))
    pipe_map.add_child(fg_p)
    pipe_map.add_child(fg_v)
    pipe_map.add_child(f.LayerControl())

    #Plot lines with colours based off risk to burst
    for i, point in enumerate(start_lats):
        f.PolyLine(((start_lats[i], start_longs[i]), (end_lats[i], end_longs[i])), color=colours[i], weight=2.5, opacity=1).add_to(pipe_map)

    #Convert to html
    pipe_map.save("map/map.html")