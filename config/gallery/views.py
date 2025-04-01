from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .forms import PictureForm
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
