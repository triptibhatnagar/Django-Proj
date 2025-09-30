# Unit 2 – Django Basics (30 Questions)

# One-Word / Objective (5 Questions)

# 31. Command used to start a new Django project.
# django-admin startproject <proj-name>

# 32. File where installed apps are registered in Django.
# settings.py

# 33. Which architecture does Django follow (3-letter acronym)?
# MVT

# 34. Default template engine in Django.
# Django Template Language (DTL)


# 35. Command used to create migrations.
# python manage.py makemigrations


# Short Answer (5 Questions)

# 36. Create a Django project named school.
# django-admin startproject school

# 37. Start a Django app called library.
# python manage.py startapp library

# 38. Register an app blog in settings.py.
# INSTALLED_APPS = [
#     ...,
#     'blog'
# ]

# 39. Write a simple Django view that returns 'Hello Django!'.
# from django.http import HttpResponse

# def hello(request):
#     return HttpResponse("Hello Django!")

# 40. Map the root URL to a view called home.
# from django.urls import path
# from . import views
# urlpatterns = [
#     path('', views.home),
# ]

# Long Coding (20 Questions)
# 41. Write the code to design a model Book with fields title, author, price. Register it in admin.py.
# models.py
# from django.db import models

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=6, decimal_places=2)

#     def __str__(self):
#         return self.title

# admin.py
# from django.contrib import admin
# from .models import Book

# admin.site.register(Book)


# 42. Write steps and code to run migrations and apply them.
# Step 1: Create migration files
# python manage.py makemigrations

# Step 2: Apply migrations to database
# python manage.py migrate

# 43. Write Django view and template to display a list of student names.
# views.py
# from django.shortcuts import render

# def student_list(request):
#     students = ["Amit", "Rahul", "Sneha", "Priya"]
#     return render(request, 'students.html', {'students': students})

# <!-- templates/students.html -->
# <h2>Student List</h2>
# <ul>
#   {% for s in students %}
#     <li>{{ s }}</li>
#   {% endfor %}
# </ul>


# 44. Create a Django form using forms.Form with fields name and email.
# forms.py
# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()


# 45. Create a Django model form for Course with title and duration.
# models.py
# class Course(models.Model):
#     title = models.CharField(max_length=100)
#     duration = models.IntegerField()
# forms.py
# from django import forms
# from .models import Course

# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['title', 'duration']


# 46. Write a Django template to loop through a list of courses and display their titles.
# templates/index.html
# <ul>
#     {% for course in courses %}
#         <li>{ course.title }</li>
#     {% endfor %}
# </ul>


# 47. Write code to configure and load static files in a Django project.
# settings.py
# STATIC_URL = "/static/"
# STATICFILES_DIRS = [BASE_DIR / "static"]

# templates/index.html
# {% load static %}
# <link rel="stylesheet" href="{% static 'style.css' %}"


# 48. Write Django template code to include style.css from static folder.
# {% load static %}
# <link rel="stylesheet" href="{% static 'style.css' %}">


# 49. Write a view function that renders template hello.html with context {'name': 'Rahul'}.
# views.py
# from django.shortcuts import render

# def hello(request):
#     return render(request, "index.html", {"name": "Rahul"})

# <!-- hello.html -->
# <h1>Hello {{ name }}</h1>

# 50. Write code to display all objects of Book model in a template using for loop.
# views.py
# from .models import Book

# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'books.html', {'books': books})

# <!-- books.html -->
# <ul>
#   {% for book in books %}
#     <li>{{ book.title }} - {{ book.author }} - {{ book.price }}</li>
#   {% endfor %}
# </ul>

# 51. Write Django view to handle GET and POST request for a feedback form.
# views.py
# from django.shortcuts import render
# from django.http import HttpResponse

# def feedback(request):
#     if request.method == "POST":
#         data = request.POST.get("feedback")
#         return HttpResponse(f"Thanks for your feedback: {data}")
#     return render(request, "feedback.html")

# <!-- feedback.html -->
# <form method="POST">
#   {% csrf_token %}
#   <textarea name="feedback"></textarea>
#   <button type="submit">Submit</button>
# </form>

# 52. Write Django code to redirect from one view to another.
# from django.shortcuts import redirect

# def old_view(request):
#     return redirect('new_view')

# def new_view(request):
#     return HttpResponse("This is new view")


# 53. Create a custom 404 error page in Django.
# settings.py
# DEBUG = False
# ALLOWED_HOSTS = ['*']

# # views.py
# def custom_404(request, exception):
#     return render(request, '404.html', status=404)

# # urls.py
# handler404 = 'myapp.views.custom_404'

# 54. Write code to use Django messages framework to display a success message.
# views.py
# from django.contrib import messages
# from django.shortcuts import render, redirect

# def submit_view(request):
#     messages.success(request, "Form submitted successfully!")
#     return redirect('home')

# <!-- template.html -->
# {% if messages %}
#   {% for msg in messages %}
#     <p>{{ msg }}</p>
#   {% endfor %}
# {% endif %}

# 55. Create a Django model Employee with name, designation, and salary fields, and add it to admin panel.
# models.py
# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     salary = models.DecimalField(max_digits=8, decimal_places=2)

# # admin.py
# from .models import Employee
# admin.site.register(Employee)


# 56. Write Django template code to show conditional statement: if marks >= 40 → Pass, else Fail.
# {% if marks >= 40 %}
#   <p>Pass</p>
# {% else %}
#   <p>Fail</p>
# {% endif %}


# 57. Write Django view and URL to display 'Welcome to Django Framework' at /welcome/.
# views.py
# from django.http import HttpResponse

# def welcome(request):
#     return HttpResponse("Welcome to Django Framework")

# # urls.py
# urlpatterns = [
#     path('welcome/', views.welcome, name='welcome'),
# ]

# 58. Write Django shell code to insert a record in the Book model.
# python manage.py shell

# from myapp.models import Book
# b = Book(title="Python Basics", author="Guido", price=299)
# b.save()

# 59. Write a Django template and view to greet user by their name entered in a form.
# views.py
# def greet(request):
#     name = ""
#     if request.method == "POST":
#         name = request.POST.get("name")
#     return render(request, "greet.html", {"name": name})

# <!-- greet.html -->
# <form method="POST">
#   {% csrf_token %}
#   <input type="text" name="name">
#   <button type="submit">Greet</button>
# </form>

# {% if name %}
#   <h2>Hello {{ name }}!</h2>
# {% endif %}


# 60. Explain Django’s MVT architecture with one example for each component (Model, View,Template).
# What is MVT Architecture?

# Django follows MVT (Model–View–Template) architecture.
# It is similar to MVC (Model–View–Controller), but here Django’s framework handles the Controller part internally, so developers mainly work with MVT.

# Model → Represents the database layer (data structure, tables, ORM mapping).
# View → Contains the business logic (handles requests, fetches data, sends response).
# Template → Handles the presentation layer (HTML, CSS, UI for users).

# Example of MVT
# 1. Model (models.py)

# We create a database model Student with name and marks.

# # models.py
# from django.db import models

# class Student(models.Model):   # Model class for Student
#     name = models.CharField(max_length=100)   # Field to store student's name
#     marks = models.IntegerField()             # Field to store student's marks

#     def __str__(self):
#         return self.name   # For better readability in Django admin


# models.Model → Base class for all Django models.
# CharField → Used for string data (student name).
# IntegerField → Used for numeric data (marks).
# __str__ → Returns name when object is printed.

# 2. View (views.py)

# We create a view to fetch students and send data to template.

# # views.py
# from django.shortcuts import render
# from .models import Student   # Import Student model

# def student_list(request):
#     students = Student.objects.all()   # Fetch all student records from DB
#     return render(request, "students.html", {"students": students})

# Student.objects.all() → ORM query to get all student data.

# render() → Combines template + data and sends response to browser.

# "students.html" → Template that will display the data.

# {"students": students} → Context dictionary (data passed to template).

# 3. Template (students.html)

# We create a template to display student names and marks.

# <!-- students.html -->
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Student List</title>
# </head>
# <body>
#     <h1>All Students</h1>
#     <ul>
#         {% for s in students %}
#             <li>{{ s.name }} - {{ s.marks }}</li>
#         {% empty %}
#             <li>No students found</li>
#         {% endfor %}
#     </ul>
# </body>
# </html>

# {% for s in students %} → Loops through student objects.

# {{ s.name }} & {{ s.marks }} → Displays student details.

# {% empty %} → If no records exist, show fallback message.

# How MVT Works Together

# User requests → /students/.
# Django URLconf routes request → student_list view.
# View fetches data from Model → Student.objects.all().
# View passes data to Template → students.html.
# Template displays data → user sees it in browser.

# ✨ In short:

# Model = Database table structure (Student).
# View = Logic to fetch and send data (student_list).
# Template = Presentation layer (students.html).