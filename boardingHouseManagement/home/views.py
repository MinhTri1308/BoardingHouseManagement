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


def back_home(request):
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def electricity(request):
    return render(request, 'pages/electricity.html')