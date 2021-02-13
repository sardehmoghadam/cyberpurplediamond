from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django import forms
from .models import contactmodel
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "temp/index.html", {

    })
class contactform(forms.Form):
    name = forms.CharField(max_length=64, label="name")
    email = forms.CharField(max_length=64, label="email")
    subject = forms.CharField(max_length=64, label="subject")
    desc = forms.CharField(max_length=1024, label="desc")

def contact(request):
    if request.method == "POST":
        # form = contactform(request.POST)
        # if form.is_valid():
            # name = form.cleaned_data["name"]
            # email = form.cleaned_data["email"]
            # subject = form.cleaned_data["subject"]
            # desc = form.cleaned_data["desc"]
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            desc = request.POST["desc"]
            f = contactmodel(name=name, email=email, subject=subject, desc=desc)
            f.save()
            return render(request, "temp/contact.html", {
                # "form": contactform()
            })
    else:
            # return render(request, "temp/contact.html",{
            #     "form": form
            # })
            return render(request, "temp/contact.html", {
                # "form": contactform()
    })
def feature(request):
    return render(request, "temp/features.html", {

    })

def news(request):
    return render(request, "temp/news.html", {

    })

def about(request):
    return render(request, "temp/about.html", {

    })

def post(request):
    return render(request, "temp/post.html", {

    })


