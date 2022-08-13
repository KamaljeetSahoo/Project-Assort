from django.shortcuts import render
from .models import Supplier, Region, Company

# Create your views here.
def homepage(request):
    if 'region' in request.GET:
        region_id = int(request.GET['region'])
        region = Region.objects.get(id=region_id)
        companies_ids = list(region.supplier_set.all().values('company').distinct())
        companies = []
        for comp in companies_ids:
            companies.append(Company.objects.get(id=comp['company']))
    else:
        companies = Company.objects.all()  
    context = {
        'suppliers': list(Supplier.objects.all())[:100],
        'companies': companies,
        'regions': Region.objects.all(),
    }
    return render(request, 'supplier/home.html', context=context)