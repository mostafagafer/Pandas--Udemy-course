import pandas as pd

headers = ['Name',	'Job Titles',	'Department',	'Full or Part-Time',
           'Salary or Hourly',	'Typical Hours',	'Annual Salary',	'Hourly Rate']

chicago = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/Pandas/lect 8 chicago salaries/Chicago_Salary.csv', header=0, names=headers)
chicago.head()
dept = chicago.groupby('Department')
dept.count().head()
dept.size().head()
