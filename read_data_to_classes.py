
import pandas as pd

from Hackathon2023Classes import Monitor


def set_up_system():

    df = pd.read_csv("data/monitorData.csv")

    monitors = [None] * len(df.index)

    for ind in df.index:
        monitors[ind] = Monitor(df["longitude"][ind],df["latitude"][ind],df["curFlow"][ind],df["avgFlow"][ind])

set_up_system()
