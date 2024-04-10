from django.shortcuts import render, redirect
from .forms import RegistrationForm 
from django.contrib.auth import logout
from room.models import Area 
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


def logout_view(request):
    logout(request)
    return redirect('home')

def create_area_home(request):
    pass