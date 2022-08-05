from django.db import models

# Create your models here.
class Region(models.Model):
    region_code = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return str(self.region_code)
    
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=10)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.supplier_name)