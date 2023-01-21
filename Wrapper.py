import read_data_to_classes as data
from map import map_new
import numpy as np

material_dict, monitors, pipes = data.set_up_system()
start_lats = np.array([])
start_longs = np.array([])
end_lats = np.array([])
end_longs = np.array([])
risks = np.array([])



for pipe in pipes:
    start_lats = np.append(start_lats, pipe.start.latitude)
    start_longs = np.append(start_longs, pipe.start.longitude)
    end_lats = np.append(end_lats, pipe.end.latitude)
    end_longs = np.append(end_longs, pipe.end.longitude)
    risk = pipe.risk()*100
    if risk<10:
        likelihood = 'green'
    elif risk<20:
        likelihood = 'yellow'
    else:
        likelihood = "red"
    risks = np.append(risks, likelihood)
print(risks)
map_new.create_map(list(start_lats), list(start_longs),
    list(end_lats), list(end_longs), list(risks))

