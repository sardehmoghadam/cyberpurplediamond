from django.shortcuts import render
from django import forms
from django.http import HttpResponse
# Create your views here.
flights = ["First", "Second"]
class newflightform(forms.Form):
    flight = forms.CharField(label="Flight Name")
def index(request):
    return render(request, "hello/index.html", {
        "flights": flights
    })
def add(request):
    if request.method == "POST":
        form = newflightform(request.POST)
        if form.is_valid():
            flight = form.cleaned_data["flight"]
            flights.append(flight)
        else:
            return render(request, "hello/add.html",{
                "form": form
            })
    return render(request, "hello/add.html", {
        "form": newflightform()
    })

# def index(request):
#     return HttpResponse("hello/index.html")