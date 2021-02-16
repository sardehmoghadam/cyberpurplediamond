from django.shortcuts import render
from django import forms
from .models import Flight
from django.http import HttpResponse
# Create your views here.
flights = ["First", "Second"]
class newflightform(forms.Form):
    source = forms.CharField(max_length=64, label="source")
    destination = forms.CharField(max_length=64, label="destination")
    price = forms.IntegerField(label="price")
def index(request):
    return render(request, "hello/index.html", {
        "flights": Flight.objects.all()
    })
def add(request):
    if request.method == "POST":
        form = newflightform(request.POST)
        if form.is_valid():
            source = form.cleaned_data["source"]
            destination = form.cleaned_data["destination"]
            price = form.cleaned_data["price"]
            f = Flight(source = source, destination = destination, price = price)
            f.save()
        else:
            return render(request, "hello/add.html",{
                "form": form
            })
    return render(request, "hello/add.html", {
        "form": newflightform()
    })

# def index(request):
#     return HttpResponse("hello/index.html")