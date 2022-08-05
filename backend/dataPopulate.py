import os, random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()
print("Dajngo module initiated")

from supplier.models import Supplier, Region
import json

data = json.load(open('../pythonScripts/data.json'))
print("Sample Json file loaded")

print("Populating Regions")
for region in data['regions']:
    print("Adding region: ", region)
    Region(region_code=region).save()
print("Populated available Regions")

print("Populating available suppliers")
regions = list(Region.objects.all())
for company in data['companies']:
    region = random.choice(regions)
    Supplier(supplier_name=company, region=region).save()
    print("Adding region: ", company)