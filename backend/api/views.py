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
    services = Service.objects.get(id=service_id)
    p=services.supplier_set.all().filter(year=2020)
    set = p.order_by('rating')[95:].values()
    radar_companies=[]
    avg_del_radar=[]
    esc_radar=[]
    for j in set:
        radar_companies.append(Company.objects.get(id=j['company_id']).company_name)
        avg_del_radar.append(j['avg_delivery_time'])
        esc_radar.append(j['escalations'])
    for i in data:
        avg_cost.append(i['avg_cost'])
        rating.append(i['rating'])
        avg_del_time.append(i['avg_delivery_time'])
        escalations.append(i['escalations'])
        resources.append(i['resources'])
    # radar_companies=['Albertsons', 'AIG', 'Apple', 'Exxon Mobil', 'Deere']
    a={
        'avg_cost':json.dumps(avg_cost),
        'rating':json.dumps(rating),
        'avg_delivery_time':json.dumps(avg_del_time),
        'escalations':json.dumps(escalations),
        'resources':json.dumps(resources),
        'radar_companies':radar_companies,
        'avg_del_radar':json.dumps(avg_del_radar),
        'esc_radar':json.dumps(esc_radar),
        'service':Service.objects.get(id=service_id).service_name,
        'company':Company.objects.get(id=company_id).company_name,
    }
  

    return render(request,'insights/insights_page.html',context=a)