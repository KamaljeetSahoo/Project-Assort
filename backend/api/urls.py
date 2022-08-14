from django.urls import path
from .views import get_data_company_year

urlpatterns = [
    path('service/<int:company_id>/<int:service_id>/', get_data_company_year),
]