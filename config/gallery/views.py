from django.shortcuts import render
from .models import Picture

def home_page(request):
    images = Picture.objects.all()
    context = { "images" : images }

    return render(request, "home.html", context)
