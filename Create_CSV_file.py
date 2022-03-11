import pandas as pd

students = pd.DataFrame([['Sameer', 1], ['Dhanush', 2], ['Pradeep', 3]], columns=['Name', 'Rollnumber'])

students.to_csv("My_Students.csv")