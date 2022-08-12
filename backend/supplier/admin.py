from django.contrib import admin
from .models import Region, Supplier, Country, Function, Service

# Register your models here.
admin.site.register(Region)
admin.site.register(Supplier)
admin.site.register(Country)
admin.site.register(Function)
admin.site.register(Service)