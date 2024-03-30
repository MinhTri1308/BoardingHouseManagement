from django import forms
import re
from .models import Room, House

class AddRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    def clean_roomsNumber(self):
        roomsNumber = self.cleaned_data['roomsNumber']
        try:
            Room.objects.get(roomsNumber=roomsNumber)
        except Room.DoesNotExist:
            return roomsNumber
        raise forms.ValidationError('Số phòng này đã có, vui lòng nhập số phòng khác')
    
    
    def save(self):
        Room.objects.create(roomsNumber=self.cleaned_data['roomsNumber'],
                            acreage=self.cleaned_data['acreage'],
                            quantity=self.cleaned_data['quantity'],
                            price=self.cleaned_data['price'],
                            interior=self.cleaned_data['interior'])
        
class UpdateInformationRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomsNumber', 'acreage', 'quantity', 'price', 'interior']

    def clean_roomsNumber(self):
        roomsNumber = self.cleaned_data['roomsNumber']
        try:
            Room.objects.get(roomsNumber=roomsNumber)
        except Room.DoesNotExist:
            return roomsNumber
        raise forms.ValidationError('Số phòng bạn vừa nhập đã có ròi, vui lòng nhập số phóng khác')
    
    
        

class DeleteRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomsNumber', 'acreage', 'quantity', 'price', 'interior']
    
    def clean_roomsNumber(self):
        roomsNumber = self.cleaned_data['roomsNumber']
        try:
            Room.objects.get(roomsNumber=roomsNumber)
        except Room.DoesNotExist:
            raise forms.ValidationError('Phòng không tồn tại, không thể xóa')
        return roomsNumber

    def deleteRoom(self):
        
        # acreage=self.cleaned_data['acreage'],
        #                     quantity=self.cleaned_data['quantity'],
        #                     price=self.cleaned_data['price'],
        #                     interior=self.cleaned_data['interior']
        roomsNumber = self.POST['roomsNumber']
        room = Room.objects.get(roomsNumber=roomsNumber)
        room.delete()


class AddHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = ['nameHouse', 'address']
    
    def clean_nameHouse(self):
        nameHouse = self.cleaned_data['nameHouse']
        try:
            House.objects.get(nameHouse=nameHouse)
        except House.DoesNotExist:
            return nameHouse
        raise forms.ValidationError('Tên nhà bạn nhập đã tồn tại, vui lòng chọn tên nhà khác')
    
    # def clean_address(self):
    #     address = self.cleaned_data['address']
    #     if not re.search(r'(\\S.*),\\s(.*),\\s(Phuong\\s.*),\\s(Quan\\s.*),\\s(Thanh pho\\s.*$)'):
    #         raise forms.ValidationError('Địa chỉ bạn nhập không hợp lệ, vui lòng nhập lại')

    def save(self):
        House.objects.create(nameHouse=self.cleaned_data['nameHouse'], address=self.cleaned_data['address'])