import re
from django.shortcuts import render
from .models import Supplier, Region

# Create your views here.
def homepage(request):
    context = {
        'supplier': Supplier.objects.all(),
        'region': Region.objects.all(),
    }
    return render(request, 'supplier/home.html', context=context)