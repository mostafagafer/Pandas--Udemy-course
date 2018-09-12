import pandas as pd

users = pd.read_csv('C:/Users/Mostafa_2/Desktop/udemy python/Pandas/ml-100k/u.user',
                    sep="|", names=['User_ID', 'Age', 'Gender', 'Occupation', 'ZIp_code'])

users  # gives all the data
users.head()  # givees the 1st 5
users.head(7)  # givees the 1st 7

users.tail()  # givees the last 5
users.tail(3)  # givees the last 3

users[10:15]  # slicing

# to extract the 1st 10 line by the Gender(for one column)
users['Gender'].head(10)


# to extract a specific column(if multible objects are needed)
col_i_want = ['Occupation', 'ZIp_code']
users[col_i_want].head()

# bolean indexation
users[users.Age > 25].head()

# bolean indexation for many objects
users[(users.Age < 40) & (users.Gender == 'M')].head()
users[(users.Occupation == 'writer') & (users.Gender == 'F')].head()
users[(users.Gender == 'M') | (users.Age > 60)].head()

# datatype
users.dtypes

users.describe()

# for setting up the index
users.set_index('User_ID').head()

# for permenantly change the index
users.set_index('User_ID', inplace=True)
users.head()

# now we can slice it
users[10:15]
# for chosing to many row use .ix[[]]
users.ix[[1, 12, 32]]
users.ix[[112, 543, 912]]
