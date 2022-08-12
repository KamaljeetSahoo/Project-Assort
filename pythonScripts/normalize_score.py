import pandas as pd
from normalize import normalize

df = pd.read_csv('datasetScore.csv')

dataframe= normalize(df,'score')
dataframe.to_csv('normalizedScore.csv',index=False)
