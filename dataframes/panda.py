# import dataframes and numpy
import numpy as np

import pandas as pd

# series with numpy linspace()
ser1 = pd.Series(np.linspace(3, 33, 3))
print(ser1)

# series with numpy linspace()
ser2 = pd.Series(np.linspace(1, 100, 10))
print(ser2)

# making data frame
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# calling head() method
# storing in new variable
data_top = data.head()
# display
print(data_top)
print(data['Name'].head(n=7))
print(data.describe())

dict = {'name': ["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["BCA", "BCA", "M.Tech", "BCA"],
        'score': [90, 40, 80, 98]}

df = pd.DataFrame(dict, index=[0, 1, 2, 3])

print(df)