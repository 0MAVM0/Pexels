from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home"),
    path('adding_page/', adding_page, name="adding_page"),
]
