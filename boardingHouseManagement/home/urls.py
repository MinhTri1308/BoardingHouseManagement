from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('choice_register/', views.choice_register, name='choice_register'),
    path('user_register/', views.user_register, name='user_register'),
    path('personnel_register/', views.personnel_register, name='personnel_register'),
    path('choice_login/', views.choice_login, name='choice_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('personnel_login/', views.personnel_login, name='personnel_login'),
    path('logout/', views.logout_view, name='logout'),
]
