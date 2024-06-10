import numpy as np
import pandas as pd


array_zeros = np.zeros((4, 3))
print("Array of zeros:", array_zeros)

array_ones = np.ones((4, 3))
print("Array of all ones:", array_ones)

array_numbers = np.arange(12).reshape((4, 3))
print("Array of numbers from 0 to 11:", array_numbers)

x = np.arange(1, 101)
F_x = 2 * x**2 + 5
print("Tabulation of F(x) = 2x^2 + 5 for x in [1, 100]:", F_x)

x2 = np.arange(-10, 11)
F_x2 = np.exp(-x2)
print("Tabulation of F(x) = e^(-x) for x in [-10, 10]:", F_x2)

url = ("https://raw.githubusercontent.com/guipsamora/pandas_exercises/"
       "master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")

df = pd.read_csv(url)
print(df.head())

df_selected = df[["Team", "Yellow Cards", "Red Cards"]]
print(df_selected.head())

num_teams = df['Team'].nunique()
print(f"Number of teams in Euro2012: {num_teams}")

teams_goals = df[["Team", "Goals"]]
print(f"Teams and goals (all):", teams_goals)

teams_more_than_6_goals = df[df['Goals'] > 6]
print(teams_more_than_6_goals[["Team", "Goals"]])
