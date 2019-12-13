"""
Source 1 (used in dropping specific rows):
https://chrisalbon.com/python/data_wrangling/pandas_dropping_column_and_rows/

Source 2 (used in dropping rows with a conditional operator):
https://stackoverflow.com/questions/13851535/delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression-involving

Source 3 (used for converting 1D arrays to 2D arrays):
https://stackoverflow.com/questions/51150153/valueerror-expected-2d-array-got-1d-array-instead
The purpose of this program is to visualize my average walking speed over
time.
_author_ = Benton Stacy
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
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
df["Start"] = df["Start"].astype("float")  # Ensures that all Start entries are
# float values.
df["Start"] /= 1000  # Change UNIX Epoch time (with ms) to UNIX Epoch time

df["End"] = df["End"].astype("float")  # Ensures that all End entries are
# float values.
df["End"] /= 1000  # Change UNIX Epoch time (with ms) to UNIX Epoch time

df["Duration"] = df["Duration"].astype("float")  # Ensures that all Duration
# entries are float values.
df["Duration"] /= 1000  # Change UNIX Epoch time (with ms) to UNIX Epoch time

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

# Only include walking data so I can do an analysis on only walking data:
df = df[df.ExerciseType == 1001]  # In my imported data, walking is
# ExerciseType "1001"
df.drop(labels=["ExerciseType"], axis=1, inplace=True)  # Remove
# ExerciseType column, now that all val's are the same

# Omit data with an abnormally slow MeanSpeed:
df.drop(df[df.MeanSpeed < 3].index, inplace=True)  # Omits all rows with
# MeanSpeed < 3 (mph)

# Omit data with an abnormally fast MaxSpeed:
df.drop(df[df.MaxSpeed > 7].index, inplace=True)  # Omits all rows with
# MaxSpeed > 7 (mph)

# Omit data with an abnorally low Distance:
df.drop(df[df.Distance < 0.3].index, inplace=True)  # Omits all rows with
# Ditance < 0.3 (miles)

# Omit data before the beginning of my time at college:
df.drop(df[df.Start < 1565582400].index, inplace=True)  # Omits all rows
# with a date before August 12th, 2019


# Data visualization of walking speed over time:

# Let's create a different version of the dataframe that will instead track
# the start column as the amount of days since August 12th, 2019.
df_day = df  # Initialize new variable
df_day["Start"] -= 1564632000  # Subtract the amount of time since August
# 1st (the intended start of my domain).
df_day["Start"] /= 86400  # Turns the units from seconds to days.

x = df_day["Start"]
y = df_day["MeanSpeed"]
graph = sns.regplot(x, y, ci=None, data=df_day, marker="+")  # Creates the
# graph.
plt.xlabel("Days since August 1st, 2019")  # X-axis label
plt.ylabel("Average walking speed (mph)")  # Y-axis label
plt.title("My Average Walking Speed While In College")  # Figure title
plt.xlim(0, 140)
plt.show()  # Prints the graph

# Splitting the data into training and test sets:
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                    random_state=0)
x_train = x_train.values.reshape(-1, 1)  # Read Source 3
x_test = x_test.values.reshape(-1, 1)
y_train = y_train.values.reshape(-1, 1)

lm = LinearRegression()  # Constructs object for LinearRegression()
reg = lm.fit(x_train, y_train)  # Conducts analysis of best fit line
m = str(reg.coef_)[2:-2]  # Eliminates [[brackets]] from slope calc
b = str(reg.intercept_)[1:-1]  # Eliminates [brackets] from y-int calc
print("y = ", m, "x + ", b, sep="")  # Prints equation of best fit line
