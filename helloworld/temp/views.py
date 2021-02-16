from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, HttpResponseRedirect, reverse
from django import forms
from .models import contactmodel, users
from .lib import hash
from django.http import HttpResponse
# Create your views here.

def index(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            flag = True
            return HttpResponseRedirect(reverse("temp:index"),{
                "flag": flag
            })
        else:
            return render(request, "temp/index.html", {
                "message": "Invalid credentials."
            })

    return render(request, "temp/index.html",{
        "flag": flag
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

def register(request):
    if request.method == "POST":
        # form = contactform(request.POST)
        # if form.is_valid():
        # name = form.cleaned_data["name"]
        # email = form.cleaned_data["email"]
        # subject = form.cleaned_data["subject"]
        # desc = form.cleaned_data["desc"]
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        store = hash(password)
        f = users(name=name, email=email, key=store[0], salt=store[1])
        f.save()
        return render(request, "temp/login.html", {
            # "form": contactform()
        })
    else:
        # return render(request, "temp/contact.html",{
        #     "form": form
        # })
        return render(request, "temp/login.html", {

    })


