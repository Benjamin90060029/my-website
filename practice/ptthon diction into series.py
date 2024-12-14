import pandas as pd
fruit = {"orange": 2 , "apple" : 3 , "grape" : 8 , "banna" : 6}
series = pd.Series(fruit)
print(series[0:3])