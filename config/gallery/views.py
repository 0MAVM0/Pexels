from django.shortcuts import render, redirect
from .forms import PictureForm
from .models import Picture

def home_page(request):
    images = Picture.objects.all()
    context = { "images" : images }

    return render(request, "home.html", context)

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

def update_image(request, id):
    image = Picture.objects.filter(id=id).first()
    if request.method == "POST":
        form = PictureForm(request.POST, instance=image)
        if form.is_valid():
            form.save()

            return redirect("home")
    else:
        form = PictureForm(instance=image)
    context = { "form" : form }

    return render(request, "edit_picture.html", context)
