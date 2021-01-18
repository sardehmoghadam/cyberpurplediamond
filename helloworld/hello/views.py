from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html", {
        # "test": False
    })

# def index(request):
#     return HttpResponse("hello/index.html")