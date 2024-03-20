from django.urls import path
from . import views
urlpatterns = [
    path('', views.create, name='electricity'),
    path('calculate/', views.calculate, name='calculate'),
]
