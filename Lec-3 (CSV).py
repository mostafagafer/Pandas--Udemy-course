import pandas as pd

pd.read_csv("TestData.csv")
pd.read_csv('TestData.csv', names=['Pizza', 'Cat', 'Dog', 'Cheese'])  # how to add header
pd.read_csv('TestData.csv', names=['Pizza', 'Cat', 'Dog', 'Cheese'],
            header=0)  # how to remove the original header

pd.read_csv("TestData.csv", usecols=['date', 'A'])  # how to chose columns from array
# or by it's position fron the array
pd.read_csv("TestData.csv", usecols=[0, 1])  # how to chose columns from array
