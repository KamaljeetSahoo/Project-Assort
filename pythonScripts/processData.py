import pandas as pd
from normalize import normalize

df = pd.read_csv('dataset.csv')

dataframe= normalize(df,'Avg. Cost')
dataframe=normalize(dataframe,'Rating')
dataframe=normalize(dataframe,'Average Delivery Time')
dataframe=normalize(dataframe,'Number of escalations')
dataframe=normalize(dataframe,'Resources')
dataframe.to_csv('dataset_normalized.csv',index=False)
