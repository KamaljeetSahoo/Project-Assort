from django.http import JsonResponse
from django.shortcuts import render
from supplier.models import Company, Service

# Create your views here.
def insights_page(request):
    return render(request, 'insights/insights_page.html')

def historical_insights(request):
    context = {
        'companies': Company.objects.all(),
    }
    return render(request, 'insights/history.html', context=context)

def company_history_view(request, company_id):
    company = Company.objects.get(id=company_id)
    suppliers = company.supplier_set.all()
    years = list(suppliers.values('year').distinct())
    context = {
        'company': company,
        'suppliers': suppliers,
        'years': years,
    }
    return render(request, 'insights/companyHistory.html', context=context)

def get_services(request, company_id):
    company = Company.objects.get(id=company_id)
    service = list(company.supplier_set.all().values('service').distinct())
    services = []
    for ser in service:
        services.append(Service.objects.get(id=ser['service']).service_name)
    return JsonResponse(services, safe=False)