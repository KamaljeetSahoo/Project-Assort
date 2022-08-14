from django.urls import path
from .views import insights_page, historical_insights, company_history_view, get_services

urlpatterns = [
    path('insights/', insights_page,name='insights_page'),
    path('history/', historical_insights, name='history'),
    path('companyHistory/<int:company_id>/', company_history_view, name='companyHistory'),
    path('api/services/<int:company_id>/', get_services),
]