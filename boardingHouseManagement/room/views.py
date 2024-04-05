from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Electricity, House
from .forms import AddRoom, UpdateInformationRoom, DeleteRoomForm, AddHouse, UpdataInformationHouse, GetRoomOfHouse, DeleteHouseForm
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


def get_rooms(request, nameHouse):
    house = House.objects.get(nameHouse=nameHouse)
    room = Room.objects.filter(house=house)
    # house = get_object_or_404(House, nameHouse=nameHouse)
    # # room = get_object_or_404(Room, nameHouse=None, id=id)
    # form = GetRoomOfHouse(instance=house)
    # if form.is_valid():
    #     form.get_room_of_house(nameHouse)
    #     return redirect('get_rooms')
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
            redirect('list_house')
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