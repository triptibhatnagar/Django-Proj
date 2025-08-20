from django.http import request, HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("this is my home page")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("this is my about page")

def contact(request):
    return HttpResponse("this is my contact page")

def help(request):
    return HttpResponse("this is my help page")

def dtl(request):
    return render(request, 'index2.html')