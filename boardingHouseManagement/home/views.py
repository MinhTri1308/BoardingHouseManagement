from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout, login, authenticate
from room.models import Personnel

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def choice_register(request):
    return render(request, 'pages/choice_register.html')

def user_register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choice_login')
    return render(request, 'pages/user_register.html', {'form': form})

def personnel_register(request):
    form = PersonnelRegister()
    if request.method == 'POST':
        form = PersonnelRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('choice_login')
    return render(request, 'pages/personnel_register.html', {'form': form})

def choice_login(request):
    return render(request, 'pages/choice_login.html')

def user_login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
            #   form.display_errors()
                return render(request, 'pages/user_login.html', {'form': form, 'message': 'Tên đăng nhập hoặc mật khẩu không hợp lệ'})
            
    return render(request, 'pages/user_login.html', {'form': form})

def personnel_login(request):
    form = PersonnelLoginForm()
    if request.method == 'POST':
        form = PersonnelLoginForm(request.POST)
        if form.is_valid():
            id_personnel = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=id_personnel, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            return render(request, 'pages/personnel_login.html', {'form': form, 'message': 'Thông tin đăng nhập không hợp lệ.'})
    return render(request, 'pages/personnel_login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')

