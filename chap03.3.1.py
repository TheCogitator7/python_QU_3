import pandas as pd

data_csv=pd.read_csv('https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv')

print(data_csv)

data_csv.to_csv('data.csv')



data_excel=pd.read_excel('https://github.com/hyunyulhenry/quant_py/raw/main/kospi.xlsx', sheet_name='kospi')

print(data_excel)

data_excel.to_excel('data.xlsx')

