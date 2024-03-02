from django.urls import path
from url_shortener.views import shortUrlView

urlpatterns = [
    path("shorturl", shortUrlView),
]