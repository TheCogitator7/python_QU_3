import pandas as pd

capital=pd.Series({
    'Korea' : 'Seoul', 
    'Japan' : 'Tokyo', 
    'China' : 'Beijing',
    'India' : 'New Delhi',
    'Taiwan' : 'Taipei',
    'Singapore' : 'Singapore'
    })

print(capital)

print(capital['Korea'])#Seoul

print(capital[['Korea', 'Taiwan']])
#Korea Seoul
#Taiwan Taipei
#dtype : object

print(capital[0])#Seoul

print(capital[[0, 3]])
#Korea Seoul
#India New Delhi
#dtype : object

print(capital[0:3])
#Korea Seoul
#Japan Tokyo
#China Beijing
#dtype : object

