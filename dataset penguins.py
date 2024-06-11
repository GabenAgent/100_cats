import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")
print(penguins.head())

sns.histplot(data=penguins, x="bill_length_mm", kde=True)
sns.barplot(data=penguins, x="species", y="body_mass_g")
sns.countplot(data=penguins, x="species")

plt.show()
