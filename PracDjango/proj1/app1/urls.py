from django.urls import path
from . import views

# localhost:8000/chai
urlpatterns = [
    path('', views.all_chai, name="all_chai"),
    # localhost:8000/chai/order/
    # path('order/', views.order, name="order"),
]