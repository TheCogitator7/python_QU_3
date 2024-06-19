import pandas as pd

dict_data={
    'col1' : [1, 2, 3, 4], 
    'col2' : [5, 6, 7, 8],
    'col3' : [9, 10, 11, 12],
    'col4' : [13, 14, 15, 16]
    }

df=pd.DataFrame(dict_data, index=['index1', 'index2', 'index3', 'index4'])

print(df)


print(df['col1'])
#index1 1
#index2 2
#index3 3
#index4 4
#Name: col1, dtype: int64

print(df.col1)#the same as above example

print(type(df['col1']))#<class 'pandas.core.series.series'>

print(df[['col1']])
#  col1
#index1 1
#index2 2
#index3 3
#index4 4


print(type(df[['col1']]))#<class 'pandas.core.frame.DataFrame'>


print(df.loc['index1'])
#col1 1
#col2 5
#col3 9
#col4 13
#Name: index1, dtype: int 64

print(df.iloc[0])
#col1 1
#col2 5
#col3 9
#col4 13
#Name: index1, dtype:int64

print(type(df.loc['index1']))
#<class 'pandas.core.series.Series'>

print(df.loc[['index1']])


print(df.iloc[[0]])


print(df.loc['index1':'index3'])

print(df.iloc[0:2])


print(df.loc['index1', 'col1'])#1


print(df.loc[['index1', 'index3'], ['col1', 'col4']])

print(df.loc['index1':'index2', 'col1':'col3'])

print(df.iloc[0, 0])#1

print(df.iloc[[0, 2], [0, 3]])

print(df.iloc[0:2, 0:3])


