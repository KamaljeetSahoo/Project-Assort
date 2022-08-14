from django.urls import path
from .views import get_data_company_year

urlpatterns = [
    path('api/getCompanyYear/<int:company_id>/<int:service_id>/', get_data_company_year),
]