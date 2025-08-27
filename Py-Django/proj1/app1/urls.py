from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('toc/', views.toc),
    path('myapp/', views.myapp),
]