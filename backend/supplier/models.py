from django.db import models

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
    
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=10)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    supplier_function = models.ForeignKey(Function, null=True, blank=True, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.supplier_name)