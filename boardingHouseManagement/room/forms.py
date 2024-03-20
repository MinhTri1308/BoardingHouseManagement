from django import forms
from .models import Room

class ValidatorRoom(forms.ModelForm):
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