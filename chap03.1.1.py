import pandas as pd

dict_data={'a' : 1, 'b' : 2, 'c' : 3}

series=pd.Series(dict_data)

print(series)
#a 1
#b 2
#c 3
#dtype : int64

print(type(series))#<class 'pandas.core.series.series'>

print(series.index)#Index(['a', 'b', 'c'], dtype='object')

print(series.values)#[1, 2, 3]



list_data=['a', 'b', 'c']

series_2=pd.Series(list_data)

print(series_2)
#0 a
#1 b
#2 c
#dtype : object



series_3=pd.Series(list_data, index=['index1', 'index2', 'index3'])

print(series_3)
#index1 a
#index2 b
#index3 c
#dtype : object

