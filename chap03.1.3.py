import pandas as pd

series_1=pd.Series([1, 2, 3])

series_2=pd.Series([4, 5, 6])

print(series_1+series_2)
#0 5
#1 7
#2 9
#dtype : int64

print(series_1*2)
#0 2
#1 4
#2 6
#dtype : int64
