from django.shortcuts import render, get_object_or_404
from .models import Electricity
# Create your views here.
def create(request):
    data = {'Electricity': Electricity.objects.all().order_by('roomsNumber')}
    return render(request, 'electricity/electricity.html', data)

def information(request, id):
    index = get_object_or_404(Electricity, id=id)
    return render(request, 'electricity/information.html', {'information': index})

def calculate(request):
    return render(request, 'electricity/calculate.html')