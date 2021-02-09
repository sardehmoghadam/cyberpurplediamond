from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "temp/index.html", {

    })
def contact(request):
    return render(request, "temp/contact.html", {

    })

# def index(request):
#     return HttpResponse("hello/index.html")