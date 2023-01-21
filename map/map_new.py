""" Core code for creating prediction plot. """

# External imports
# Folium uses python and translates it to html/css/javascript for the browser
import math
import folium as f

def create_map(start_lats, start_longs, end_lats, end_longs, colours, risks):

    #Create a map using folium, using lattitude and longitude coords, the tile changes the map type
    pipe_map = f.Map(location=[start_lats[0],start_longs[0]], tiles="Stamen Terrain", zoom_start=13)

    # Create feature groups for each layer
    fg_m = f.FeatureGroup(name="Monitors")
    fg_p = f.FeatureGroup(name="Pipes")

    # Add multiple markers for monitors
    for lt, ln in zip(start_lats, start_longs):
        fg_m.add_child(f.Marker(location=[lt,ln],
        popup="Monitor with coordinates "+str(lt)+", "+str(ln),
        icon=f.Icon(icon='droplet', prefix='fa', color="black")))
        #colours += [colour_icon(li)]

    #Add base map and points
    pipe_map.add_child(fg_m)
    pipe_map.add_child(fg_p)
    pipe_map.add_child(f.LayerControl())

    #Plot lines with colours based off risk to burst
    for i, point in enumerate(start_lats):
        fg_p.add_child(f.PolyLine(((start_lats[i], start_longs[i]),(end_lats[i], end_longs[i])),
        color=colours[i], weight=4.5, opacity=1, popup="Pipe with risk factor "+str(round(risks[i],3))))

    #Convert to html
    pipe_map.save("map/map.html")