from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Electricity, House, Personnel, Area
from .forms import AddRoom, UpdateInformationRoom, DeleteRoomForm, AddHouse, UpdataInformationHouse, DeleteHouseForm, AddPersonnel, UpdateInformationPersonnel, DeletePersonnel, AddArea, UpdateArea, DeleteArea
# Create your views here.
#Room
def create_room(request):
    data = {'Room': Room.objects.all().order_by('roomsNumber')}
    return render(request, 'rooms/list_room.html', data)

def get_information_room(request, id):
    information_room = get_object_or_404(Room, id=id)
    return render(request, 'rooms/information_room.html', {'inf_room': information_room})

def add_room(request):
    form = AddRoom()
    if request.method == 'POST':
        form = AddRoom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/add_room.html', {'new_room': form})

def edit_room(request, id):
    room = get_object_or_404(Room, id=id)
    form = UpdateInformationRoom(instance=room)
    if request.method == 'POST':
        form = UpdateInformationRoom(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('list_room')
    return render(request, 'rooms/edit_room.html', {'update_room': form, 'inf_room': room})

def delete_room(request, id):
    room = get_object_or_404(Room, id=id)
    form = DeleteRoomForm(instance=room)
    if request.method == 'POST':
        form = DeleteRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.deleteRoom(id)
            return redirect('list_room')
    return render(request, 'rooms/delete_room.html', {'delete_room': form ,'inf_room': room})

def information(request, id):
    index = get_object_or_404(Electricity, id=id)
    return render(request, 'rooms/information.html', {'inf_electricity': index})

#House
def create_house(request):
    data = {'House': House.objects.all()}
    return render(request, 'rooms/list_house.html', data)

def get_information_house(request, nameHouse):
    house = get_object_or_404(House, nameHouse=nameHouse)
    return render(request, 'rooms/information_house.html', {'inf_house': house})


def get_rooms(request, nameHouse):
    house = House.objects.get(nameHouse=nameHouse)
    room = Room.objects.filter(house=house)
    return render(request, 'rooms/house_of_list_rooms.html', {'inf_house': house, 'room_of_house': room})

def add_house(request):
    form = AddHouse()
    if request.method == 'POST':
        form = AddHouse(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_house')
    return render(request, 'rooms/add_house.html', {'new_house': form})

def edit_house(request, nameHouse):
    house = get_object_or_404(House, nameHouse=nameHouse)
    form = UpdataInformationHouse(instance=house)
    if request.method == 'POST':
        form = UpdataInformationHouse(request.POST, instance=house)
        if form.is_valid():
            form.save()
            return redirect('list_house')
    return render(request, 'rooms/edit_house.html', {'update_house': form, 'inf_house': house})

def delete_house(request, nameHouse):
    house = get_object_or_404(House, nameHouse=nameHouse)
    form = DeleteHouseForm(instance=house)
    if request.method == 'POST':
        form = DeleteHouseForm(request.POST, instance=house)
        if form.is_valid():
            form.deleteHouse(nameHouse)
            return redirect('list_house')
    return render(request, 'rooms/delete_house.html', {'delete_house': form, 'inf_house': house})

#Electricity
def create_electricity(request):
    data = {'Electricity': Electricity.objects.all(), 'House': House.objects.all()}
    return render(request, 'rooms/electricity.html', data)

def calculate(request):
    data = House.objects.all()
    return render(request, 'rooms/calculate.html', {'inf_house': data})


#Personnel
def create_personnel(request):
    data = {'Personnel': Personnel.objects.all()}
    return render(request, 'rooms/list_personnel.html', data)

def get_information_personnel(request, fullname):
    personnel = get_object_or_404(Personnel, fullname=fullname)
    return render(request, 'rooms/information_personnel.html', {'inf_personnel': personnel})

def add_personnel(request):
    form = AddPersonnel()
    if request.method == 'POST':
        form = AddPersonnel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_personnel')
    return render(request, 'rooms/add_personnel.html', {'new_personnel': form})

def edit_personnel(request, fullname):
    personnel = get_object_or_404(Personnel, fullname=fullname)
    form = UpdateInformationPersonnel(instance=personnel)
    if request.method == 'POST':
        form = UpdateInformationPersonnel(request.POST, instance=personnel)
        if form.is_valid():
            form.save()
            return redirect('list_personnel')
    return render(request, 'rooms/edit_personnel.html', {'update_personnel': form, 'inf_personnel': personnel})

def delete_personnel(request, fullname):
    personnel = get_object_or_404(Personnel, fullname=fullname)
    form = DeletePersonnel(instance=personnel)
    if request.method == 'POST':
        form = DeletePersonnel(request.POST, instance=personnel)
        if form.is_valid():
            form.deletePersonnel(fullname)
            return redirect('list_personnel')
    return render(request, 'rooms/delete_personnel.html', {'delete_personnel': form, 'inf_personnel': personnel})


#Area
def create_area(request):
    data = {'Area': Area.objects.all().order_by('id')}
    return render(request, 'rooms/list_area.html', data)

def add_area(request):
    form = AddArea()
    if request.method == 'POST':
        form = AddArea(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_area')
    return render(request, 'rooms/add_area.html', {'add_area': form})

def edit_area(request, id):
    area = get_object_or_404(Area, id=id)
    form = UpdateArea(instance=area)
    if request.method == 'POST':
        form = UpdateArea(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('list_area')
    return render(request, 'rooms/edit_area.html', {'update_area': form, 'inf_area': area})

def delete_area(request, id):
    area = get_object_or_404(Area, id=id)
    form = DeleteArea(instance=area)
    if request.method == 'POST':
        form = DeleteArea(request.POST, instance=area)
        if form.is_valid():
            form.deleteArea(id)
            return redirect('list_area')
    return render(request, 'rooms/delete_area.html', {'delete_area': form, 'inf_area': area})