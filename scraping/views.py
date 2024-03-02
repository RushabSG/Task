from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

def nifty_view(request):
    nifty50_data = cache.get('nifty50_data', {})
    return render(request, 'nifty.html', {'nifty50_data': nifty50_data})