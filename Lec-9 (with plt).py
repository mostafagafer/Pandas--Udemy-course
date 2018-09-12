import pandas as pd


col1 = ['user_id', 'movie_id', 'rating', 'unix_timestamp']

rating = pd.read_csv('C:/Users/Mostafa_2/Desktop/udemy python/Pandas/ml-100k/u.data',
                     sep="\t", names=col1)
rating.head()


col2 = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('C:/Users/Mostafa_2/Desktop/udemy python/Pandas/ml-100k/u.item',
                     sep='|', names=col2, usecols=range(5), encoding="ISO-8859-1")
# encoding because the file is coded
movies.head()
movie_rating = pd.merge(movies, rating)
movie_rating.head()


u_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_csv('C:/Users/Mostafa_2/Desktop/udemy python/Pandas/ml-100k/u.user',
                    sep="|", names=u_cols)
users.head()
lens = pd.merge(movie_rating, users)
lens.head()

# top 20 title is mentioned
most_rated = lens.groupby('title').size().sort_values(ascending=False)[:20]
most_rated
# or by
lens.title.value_counts()[:20]


import numpy as np
movies_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
movies_stats.head()
movies_stats.sort_values([('rating', 'mean')], ascending=False).head()


# to plot it in Histogram

import matplotlib.pyplot as plt

users.age.hist(bins=30)

plt.title("Distrebution of users age")
plt.xlabel('Age')
plt.ylabel('Count of users')
plt.show()

# to draw a bar graph for M vs F . 1st chose the most popular 50 moveis
most_50 = lens.groupby('movie_id').size().sort_values(ascending=False)[:50]
most_50
pivoted = lens.pivot_table(index=['movie_id', 'title'], columns=[
                           'gender'], values='rating', fill_value=0)
pivoted


pivoted['diff'] = pivoted.M-pivoted.F
pivoted.head()
pivoted.reset_index('movie_id', inplace=True)
disagreament = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
disagreament.head()

plt.title('Male vs Femal average ratings\n Where Difference is >0= favorited by men')
plt.xlabel('Average rating Difference')
plt.ylabel('Title')
disagreament.sort_values().plot(kind='barh', figsize=[10, 15])
plt.show()
