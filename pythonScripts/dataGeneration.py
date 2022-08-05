from math import nan
import pandas as pd
import json

df = pd.read_excel('Book1.xlsx')
companies, regions, services = [], [], []
for val in df['Companies'].values:
    if type(val)==str:
        companies.append(val)
for val in df['Services'].values:
    if type(val)==str:
        services.append(val)
for val in df['Region'].values:
    if type(val)==str:
        regions.append(val)

j = {
    'companies': companies,
    'regions': regions,
    'services': services,
}
with open('data.json','w') as out:
    json.dump(j, out, indent=4)