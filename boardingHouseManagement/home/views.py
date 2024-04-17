from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import logout, login, authenticate
from room.models import Personnel

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def register(request):
    form = RegistrationForm()
    success = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            return redirect('login', {'register_successfully': success})
    return render(request, 'pages/register.html', {'form': form})

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
            #     form.display_errors()
                return render(request, 'pages/user_login.html', {'form': form, 'message': 'Tên đăng nhập hoặc mật khẩu không hợp lệ'})
            
    return render(request, 'pages/user_login.html', {'form': form})

def personnel_login(request):
    form = PersonnelLoginForm()
    if request.method == 'POST':
        form = PersonnelLoginForm(request.POST)
        if form.is_valid():
            id_personnel = form.cleaned_data['id_personnel']
            phone = form.cleaned_data['phone']
            personnel = authenticate_personnel(id_personnel=id_personnel, phone=phone)
            if personnel is not None:
                login(request, personnel)
                return redirect('home')   # Thay 'home' bằng tên view hoặc đường dẫn muốn chuyển hướng
        else:
            # Xử lý trường hợp thông tin đăng nhập không hợp lệ
            # Trả về form với thông báo lỗi
            return render(request, 'pages/personnel_login.html', {'form': form, 'message': 'Thông tin đăng nhập không hợp lệ.'})
     
    return render(request, 'pages/personnel_login.html', {'form': form})

def authenticate_personnel(id_personnel, phone):
    try:
        personnel = Personnel.objects.get(id_personnel=id_personnel, phone=phone)
    except Personnel.DoesNotExist:
        return None
    return personnel

def logout_view(request):
    logout(request)
    return redirect('home')

