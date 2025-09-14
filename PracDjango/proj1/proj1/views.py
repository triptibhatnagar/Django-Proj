# user --> req --> urls.py --> views.py --> res --> user

from django.http import HttpResponse
from django.shortcuts import render # for rendering html pgs

def home(request):
    # return HttpResponse("Hello Django, this is homepage")
    # return render(request, 'index.html')
    return render(request, 'website/index.html')
    # templates to tumhe pta hee h, bs vhi se ye file utha lo

def about(request):
    return HttpResponse("Hello Django, this is about page")
    # return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("Hello Django, this is contact page")
    # return render(request, 'website/contact.html')