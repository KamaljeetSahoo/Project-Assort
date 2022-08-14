from django.urls import path
from .views import service,viewcompany 

urlpatterns = [
    path('services/',service,name='service'),
    path('service/<int:service_id>/', viewcompany, name="viewcompany"),
   
]   