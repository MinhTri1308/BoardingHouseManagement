from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('back_home/', views.back_home, name='back_home'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('electricity_index/', views.electricity, name='electricity'),
]
