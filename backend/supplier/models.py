from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Region(models.Model):
    region_code = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return str(self.region_code)

class Country(models.Model):
    country_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.country_name)

class Function(models.Model):
    company_func = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.company_func)
    
class Service(models.Model):
    service_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return str(self.service_name)

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    
class Supplier(models.Model):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    supplier_function = models.ForeignKey(Function, null=True, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE)
    avg_cost = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(100), MinValueValidator(60)])
    avg_delivery_time = models.IntegerField(blank=True, null=True)
    escalations = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    resources = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return str(self.supplier_name)