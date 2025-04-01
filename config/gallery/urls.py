from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('adding_page/', adding_page, name="adding_page"),
    path("update/<int:id>/", update_image, name="update_image"),
    path("delete/<int:id>/", delete_image, name="delete_image"),
]
