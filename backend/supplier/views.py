import re
from django.shortcuts import render
from .models import Supplier, Region,Company

# Create your views here.
def homepage(request):
    print(Company.objects.all())
    context = {
        'suppliers': list(Supplier.objects.all())[:100],
    }
    return render(request, 'supplier/home.html', context=context)