import pandas as pd

df = pd.read_csv("FuelConsumption.csv")

print(df.tail(10))   # we also use .tail()  to print last 5 items