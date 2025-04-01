from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import PictureForm
from django.views import View
from .models import Picture

'''
def home_page(request):
    images = Picture.objects.all()
    context = { "images" : images }

    return render(request, "home.html", context)

class HomePageView(View):
    def get(self, request):
        images = Picture.objects.all()
        context = { "images" : images }

        return render(request, "home.html", context)
'''

class HomePageView(ListView):
    model = Picture
    template_name = "home.html"
    context_object_name = "images"

class AddPhotoView(View):
    def post(self, request):
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect("home")

        context = { "form" : form }

        return render(request, "adding_picture.html", context)

    def get(self, request):
        form = PictureForm()

        context = { "form" : form }

        return render(request, "adding_picture.html", context)

'''
def adding_page(request):
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = PictureForm()
    context = { "form" : form }

    return render(request, "adding_picture.html", context)
'''

def update_image(request, id):
    image = Picture.objects.filter(id=id).first()
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = PictureForm(instance=image)
    context = { "form" : form }

    return render(request, "edit_picture.html", context)

def delete_image(request, id):
    image = Picture.objects.filter(id=id).first()
    if image:
        image.delete()

        return redirect("home")

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "user/signup.html"
    success_url = reverse_lazy("login")

class CustomLoginView(LoginView):
    template_name = "user/login.html"