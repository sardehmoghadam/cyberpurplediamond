from django.contrib.auth import login, logout, authenticate
from .models import contactmodel
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    # if request.method == "POST":
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         flag = True
    #         return HttpResponseRedirect(reverse("temp:index"),{
    #             "flag": flag
    #         })
    #     else:
    #         return render(request, "temp/index.html", {
    #             "message": "Invalid credentials."
    #         })

    return render(request, "temp/index.html",{
        "flag": flag
    })

def contact(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
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
            f = contactmodel(name=name, email=email, subject=subject, desc=desc, readed=False)
            f.save()
            return render(request, "temp/contact.html", {
                "flag": flag
            })
    else:
            # return render(request, "temp/contact.html",{
            #     "form": form
            # })
            return render(request, "temp/contact.html", {
                "flag": flag
    })
def feature(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/features.html", {
        "flag": flag
    })

def news(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/news.html", {
        "flag": flag
    })
def about(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/about.html", {
        "flag": flag
    })

def post(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
    return render(request, "temp/post.html", {
        "flag": flag
    })

def register(request):
    flag = False
    if not request.user.is_authenticated:
        flag = True
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
            "flag": flag
    })

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("temp:index"))

def logging(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("temp:index"), {
                "message": "Valid credentials"
            })
        else:
            return render(request, "temp/index.html", {
                "message": "Invalid credentials."
            })

    return HttpResponseRedirect(reverse("temp:index"))
