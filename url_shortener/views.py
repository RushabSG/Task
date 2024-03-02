from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners
from url_shortener.models import ShortUrlModel
from django.contrib import messages
# Create your views here.


def shortUrlView(request):
    try:
        short_url = ''
        url = ''
        if request.method == "POST":
            shortener = pyshorteners.Shortener()
            url = request.POST.get("url")
            short_url = shortener.tinyurl.short(url)
            messages.success(request, "Generated")
            ShortUrlModel.objects.create(original_url=url, short_url=short_url)
            
        return render(request, "urlshortener.html", {"short_url": short_url, "url": url}, status=201)
    except:
        return HttpResponse({"Bad request"}, status=400)
