import pandas as pd

employee_data = pd.DataFrame([[3, 'Abinandh', 'Software', 50000, 'TCS'], [7, 'Sameer', 'Software', 30000, 'Harman'], \
                              [9, 'Pradeep', 'Hardware', 40000, 'Wipro'], [4, 'Dhanush', 'Embedded', 60000, 'ALM']],\
columns=['Employee Code', 'Employee Name', 'Employee Deisgnation', 'Employee Salary', 'Employee Company Name'])

employee_data.to_csv("employees.csv")