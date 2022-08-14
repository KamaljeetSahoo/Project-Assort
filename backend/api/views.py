from django.shortcuts import render
from supplier.models import Company, Service, Supplier
from django.http import JsonResponse
import json
# Create your views here.
def get_data_company_year(request, company_id, service_id):
    # print(dir(request))
    suppliers = Supplier.objects.filter(company_id=company_id)
    data = suppliers.values().filter(service=service_id)
    avg_cost=[]
    rating=[]
    avg_del_time=[]
    escalations=[]
    resources=[]
    for i in data:
        avg_cost.append(i['avg_cost'])
        rating.append(i['rating'])
        avg_del_time.append(i['avg_delivery_time'])
        escalations.append(i['escalations'])
        resources.append(i['resources'])
    a={
        'avg_cost':json.dumps(avg_cost),
        'rating':json.dumps(rating),
        'avg_delivery_time':json.dumps(avg_del_time),
        'escalations':json.dumps(escalations),
        'resources':json.dumps(resources)
    }
  

    return render(request,'insights/insights_page.html',context=a)