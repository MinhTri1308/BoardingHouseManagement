from django.shortcuts import render, redirect
from .forms import RegistrationForm 
from django.contrib.auth import logout
# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'pages/register.html', {'form': form})

# def login(request):
#     form_login = RegistrationForm()
#     if request.method == 'POST':
#         form_login = RegistrationForm(request.POST)
#         if form_login.is_valid():
#             form_login.save()
#             return redirect('home')
#     return render(request, 'pages/login.html', {'form': form_login})

def back_home(request):
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')