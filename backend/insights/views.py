from django.shortcuts import render

# Create your views here.
def insights_page(request):
    return render(request, 'insights/insights_page.html')