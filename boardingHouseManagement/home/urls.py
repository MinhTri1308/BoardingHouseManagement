from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('choice_login/', views.choice_login, name='choice_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('personnel_login/', views.personnel_login, name='personnel_login'),
    path('logout/', views.logout_view, name='logout'),
]
