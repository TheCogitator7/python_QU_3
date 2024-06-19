import pandas as pd

dict_data={
    'col1' : [1, 2, 3],
    'col2' : [4, 5, 6],
    'col3' : [7, 8, 9]
    }
df=pd.DataFrame(dict_data)
print(df)

print(type(df))#<class 'pandas.core.frame.DataFrame'>


df2=pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(df2)



df3=pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['index1', 'index2', 'index3'], columns=['col1', 'col2', 'col3'])

print(df3)


df3.index=['행1', '행2', '행3']
df3.columns=['열1', '열2', '열3']

print(df3)

df3.rename(index={'행1' : 'row 1'}, inplace=True)
df3.rename(columns={'열1' : 'column 1'}, inplace=True)

print(df3)

df3.drop('행3', axis=0, inplace=True)
df3.drop('열3', axis=1, inplace=True)

print(df3)
