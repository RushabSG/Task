from django.urls import path
from .views import nifty_view

urlpatterns = [
    path('nifty/', nifty_view, name='nifty50'),
]