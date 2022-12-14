import os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()
print("Dajngo module initiated")

from supplier.models import Supplier, Region, Country, Function, Service, Company
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
regions = df['Region'].unique()
countries = df['Country'].unique()
functions = df['Function'].unique()
services = df['Service'].unique()
companies = df['Supplier Name'].unique()

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

print("Adding Companies")
for comp in companies:
    Company(company_name=comp).save()
    print("Adding Company: ", comp)

print("Sample data added to the database")

for i, row in df.iterrows():
    func = Function.objects.get(company_func=row['Function'])
    service = Service.objects.get(service_name=row['Service'])
    country = Country.objects.get(country_name=row['Country'])
    region = Region.objects.get(region_code=row['Region'])
    company = Company.objects.get(company_name=row['Supplier Name'])
    Supplier(company=company, region=region, country=country, supplier_function=func, service=service, avg_cost=row['Avg. Cost'], rating=row['Rating'], avg_delivery_time=row['Average Delivery Time'], escalations=row['Number of escalations'], year=row['Year'], resources=row['Resources']).save()
    print("Adding supplier: ", row['Supplier Name'])