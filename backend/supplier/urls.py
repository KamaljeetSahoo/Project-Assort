from django.urls import path
from .views import homepage, viewCompanyData, fetch

urlpatterns = [
    path('', homepage, name='home'),
    path('companyData/<int:company_id>/', viewCompanyData, name="companyData"),
    path('fetch/', fetch),
]