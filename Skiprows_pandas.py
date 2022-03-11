import pandas as pd

df = pd.read_csv("FuelConsumption.csv", skiprows=[1])  # it skips the row of 0th position of model year !!!****

print(df.head())