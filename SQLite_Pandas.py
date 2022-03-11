import pandas as pd

import sqlite3

connection = sqlite3.connect("mobile.db")

df = pd.read_sql_query("Select * from Smart_phones", connection)

print(df)  # we can also use df.info() & df.head() & df.tail()  for any purpose at any time!!! ***