"""
Source 1 (used in dropping specific rows):
https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

path = "C:\\Users\\bento\\Documents\\COP1500-PersonalProject_1\\ExerciseData" \
       ".csv"
df = pd.read_csv(path)


# Pre-processing Data:

# Remove NaN's which could cloud the data:
df.dropna(subset=["MeanSpeed"], axis=0, inplace=True)  # Removes data entries
# which don't have a MeanSpeed entry.
df.dropna(subset=["MaxSpeed"], axis=0, inplace=True)  # Removes data entries
# which don't have a MaxSpeed entry.
df.dropna(subset=["Distance"], axis=0, inplace=True)  # Removes data entries
# which don't have a Distance entry.
df.dropna(subset=["Calories"], axis=0, inplace=True)  # Removes data entries
# which don't have a Calories entry.

# Format all relevant data so proper analysis can be made:
df["MeanSpeed"] = df["MeanSpeed"].astype("float")  # Ensures that all
# MeanSpeed entries are float values.
df["MeanSpeed"] *= 2.23694  # Converts MeanSpeed from meters per second to
# miles per hour

df["MaxSpeed"] = df["MaxSpeed"].astype("float")  # Ensures that all
# MaxSpeed entries are float values.
df["MaxSpeed"] *= 2.23694  # Converts MaxSpeed from meters per second to
# miles per hour

df["Distance"] = df["Distance"].astype("float")  # Ensures that all
# Distance entries are float values.
df["Distance"] /= 1609.344  # Converts Distance from meters to miles

df["Calories"] = df["Calories"].astype("float")  # Ensures that all
# Calories entries are float values.

df["Start"] /= 1000  # Change UNIX Epoch time (with ms) to UNIX Epoch time
df["End"] /= 1000  # Change UNIX Epoch time (with ms) to UNIX Epoch time

# Only include walking data so I can do an analysis on only walking data:
df = df[df.ExerciseType == 1001]  # In my imported data, walking is
# ExerciseType "1001"

print(df.head(50))