import pandas as pd

user_data = pd.DataFrame([['Abinandh', 'Madurai', 'Male', 833456783, 'abinandhmadi@gmail.com', 'abinandh2000', 'abikshaya'],\
                              ['Sameer', 'Karur', 'Male', 8220062948, 'arijitsameers@gmail.com', 'sherlocksameeer', 'sherlock17'], \
                              ['Dhanush', 'Hosur', 'Male', 9344567890, '3dhannushkccd@gmail.com', 'dhanush10', 'dhanush33']] \
                               , columns=['Name', 'Address', 'Gender', 'Mobile Number', 'Email ID', 'User ID', 'Password'])

user_data.to_csv("user.csv")