import os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()
print("Dajngo module initiated")

from supplier.models import Supplier, Region, Country, Function, Service
# import json

# data = json.load(open('../pythonScripts/data.json'))
# print("Sample Json file loaded")

# print("Populating Regions")
# for region in data['regions']:
#     print("Adding region: ", region)
#     Region(region_code=region).save()
# print("Populated available Regions")

# print("Populating available suppliers")
# regions = list(Region.objects.all())
# for company in data['companies']:
#     region = random.choice(regions)
#     Supplier(supplier_name=company, region=region).save()
#     print("Adding region: ", company)

import pandas as pd
df = pd.read_csv('../pythonScripts/dataset.csv')
print("Sample Data Loaded")
print(df.head())
print(df.columns)
suppliers = df['Supplier Name'].unique()
regions = df['Region'].unique()
countries = df['Country'].unique()
functions = df['Function'].unique()
services = df['Service'].unique()

print("Adding regions")
for region in regions:
    Region(region_code = region).save()
    print("Adding Region: ", region)

print("Adding Countries")
for country in countries:
    Country(country_name = country).save()
    print("Adding country: ", country)

print("Adding Functions")
for func in functions:
    Function(company_func=func).save()
    print("Adding function: ", func)

print("Adding Services")
for service in services:
    Service(service_name=service).save()
    print("Adding service: ", service)

print("Sample data added to the database")