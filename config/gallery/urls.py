from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('adding_page/', AddPhotoView.as_view(), name="adding_page"),
    path("update/<int:id>/", EditPictureView.as_view(), name="update_image"),
    path("delete/<int:id>/", delete_image, name="delete_image"),
    path("signup/", SignUpView.as_view(), name="registrate"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
