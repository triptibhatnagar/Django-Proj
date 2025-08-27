from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello")

def toc(request):
    return HttpResponse("toc")

def myapp(request):
    return render(request, "app1.html")