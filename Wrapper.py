""" Wrapper script, which generates the html plot,
indicating the risk of bursting/leaks for each pipe. """

# External imports
import numpy as np

# Local imports
from map import map_new
import read_data_to_classes as data

# Read in point locations and risk model
material_dict, monitors, pipes = data.set_up_system()
start_lats = np.array([])
start_longs = np.array([])
end_lats = np.array([])
end_longs = np.array([])
risks_colours = np.array([])
risks = np.array([])

# Format class data and risk probability into arrays
for pipe in pipes:

    start_lats = np.append(start_lats, pipe.start.latitude)
    start_longs = np.append(start_longs, pipe.start.longitude)
    end_lats = np.append(end_lats, pipe.end.latitude)
    end_longs = np.append(end_longs, pipe.end.longitude)

    # Assign colours to pipes based off risk of leakage
    if pipe.risk()<0.1:
        likelihood = 'green'
    elif pipe.risk()<0.2:
        likelihood = 'yellow'
    else:
        likelihood = "red"
    risks_colours = np.append(risks_colours, likelihood)
    risks = np.append(risks, pipe.risk())
# Create and save html map of sessor locations and pipes
map_new.create_map(list(start_lats), list(start_longs),
    list(end_lats), list(end_longs), list(risks_colours), list(risks))