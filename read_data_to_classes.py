
# External imports
import pandas as pd

# Internal imports
from water_system_classes import Monitor, pipe, material

def set_up_system():
    """ Read in our theoretical datasets and put them in their respective classes """

    # Load material data
    material_dict = {}
    materialsdf = pd.read_csv("data/materialData.csv", index_col="Material")

    for i in materialsdf.index:
        material_dict[i] = material(materialsdf.loc[i]["ChemicalErosionFactor"], materialsdf.loc[i]["WaterErosionFactor"], materialsdf.loc[i]["Strength"])



    # Set up all our monitors
    df = pd.read_csv("data/monitorData.csv")
    monitors = [None] * len(df.index)

    for ind in df.index:
        monitors[ind] = Monitor(df["longitude"][ind],df["latitude"][ind],df["curFlow"][ind],df["avgFlow"][ind])


    # Set up all our pipes
    pipesdf = pd.read_csv("data/pipedata.csv")

    pipes = [None] * len(pipesdf.index)
    for ind in pipesdf.index:
        pipes[ind] = pipe(monitors[pipesdf["pipe_start"][ind]-1],
            monitors[pipesdf["pipe_end"][ind]-1],pipesdf["depth"][ind],
            pipesdf["fluid"][ind], material_dict[pipesdf["material"][ind]],
            pipesdf["date_installed"][ind])

    return material_dict, monitors, pipes
