from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def education(request):
    return render(request, "education.html")

def projects(request):
    return render(request, "projects.html")

def skills(request):
    return render(request, "skills.html")
