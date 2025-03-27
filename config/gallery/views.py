from django.shortcuts import render
from .models import Picture

def home_page(request):
    return render(request, "home.html")
