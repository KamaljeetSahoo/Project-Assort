from django.shortcuts import render
from supplier.models import Service ,Company
# Create your views here.
def service(request):
    s = Service.objects.all()
    context={
        'services':s,
    }
    return render(request,'services/services_page.html',context=context)

def viewcompany(request,service_id):

    c=Company.objects.all()
    context={
        'companies':c,
        "s_id":service_id,
    }

    return render(request,'services/viewcompany.html',context=context)