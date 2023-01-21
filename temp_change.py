
import pandas as pd

def temp_change():

    # In the long term, we will have a dataset for temperature variation for each region
    temp_data = pd.read_csv("data/weather.csv")

    # Record when the maximum temperature is above zero and when the minimum is below
    temp_data["Positive"] = temp_data["Maximum daily air temperature"] >= 0
    temp_data["Negative"] = temp_data["Minimum daily air temperature"] <= 0

    # Work out when both a positive and negative temperature is recorded in a day
    temp_data["freeze_thaw"] = temp_data["Positive"] & temp_data["Negative"]

    chance_of_thaw_in_day = temp_data["freeze_thaw"].sum() / temp_data.shape[0]

    return chance_of_thaw_in_day
