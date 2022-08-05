from django.db import models

# Create your models here.
region_choices = [
    ('AMEA','AMEA'),
    ('AMER','AMER'),
    ('AMS','AMS'),
    ('ANZ','ANZ'),
    ('ANZIT','ANZIT'),
    ('ANZUK','ANZUK'),
    ('APAC','APAC'),
    ('APEC','APEC'),
    ('APJ','APJ'),
    ('APMA','APMA'),
    ('APSG','APSG'),
    ('AU','AU'),
    ('ASEAN','ASEAN'),
    ('AUKUS','AUKUS'),
]
class Region(models.Model):
    region_code = models.CharField(max_length=10, choices=region_choices, default='AMEA')
    
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=10)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)