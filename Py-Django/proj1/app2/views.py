from django.shortcuts import render
from django.http import request

# Create your views here.
def home(request):
    students = [
        {'name': 'a', 'email':'a123@gmail.com', 'marks': 45},
        {'name': 'a', 'email':'a123@gmail.com', 'marks': 45},
        {'name': 'a', 'email':'a123@gmail.com', 'marks': 45}
    ]
    return render(request, 'home.html', {'students': students})