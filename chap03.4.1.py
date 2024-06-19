import pandas as pd
import seaborn as sns

df=sns.load_dataset('titinic')
print(df.head())

print(df.tail())

print(df.shape)

print(df.info())

print(df['sex'].value_counts())

print(df[['sex', 'survived']].value_counts())

print(df[['sex', 'survived']].value_counts(normalize=True).sort_index())

print(df['survived'].mean())

print(df[['survived', 'age']].mean())

print(df['fare'].min())

print(df['fare'].max())

print(df['fare'].mean())

print(df['fare'].median())

