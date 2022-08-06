import re
from django.shortcuts import render
from .models import Supplier, Region

# Create your views here.
def homepage(request):
    context = {
        'suppliers': Supplier.objects.all(),
        'regions': Region.objects.all(),
    }
    return render(request, 'supplier/home.html', context=context)