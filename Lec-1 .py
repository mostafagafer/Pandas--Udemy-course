import pandas as pd

s = pd.Series([10, "Namaste", 23.5, "Hello"])
print(s)
# now we can index it
s[0]
s[1]
# for indexing it by a,b,c,d rather than 0,1,2,3
s = pd.Series([10, "Namaste", 23.5, "Hello"], index=['a', 'b', 'c', 'd'])
print(s)
s['a']
s['b']

# By deict
d = {"Seattle": 1000000, "San Francesco": 5000000, "San Jose": 1500000}
cities = pd.Series(d)
print(cities)
cities["Seattle"]
cities[cities > 1000000]
cities[cities == 1000000]

####
d = {"Seattle": 100, "San Francesco": 500, "San Jose": 150, "London": 1200, "Tokyo": 1600}
cities = pd.Series(d)
cities
cities < 1000
# how to change San francesco from 500 to 600
cities["San Francesco"] = 600
print(cities)
# how to change many cities to 750
cities[cities < 1000] = 750
cities
# divideng all cities by 10
cities/10

# if you want to square them , import numpy
import numpy as np
np.square(cities)

# checking if all the cities has value
cities.isnull()
