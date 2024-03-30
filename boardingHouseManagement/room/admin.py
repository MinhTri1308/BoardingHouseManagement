from django.contrib import admin
from .models import Room, Electricity, House, Guests
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ['roomsNumber', 'acreage']
    list_filter = ['acreage']
    search_fields = ['roomsNumber', 'acreage']


admin.site.register(Room, RoomAdmin)

class GuestsAdmin(admin.ModelAdmin):
    list_display = ['room', 'fullname']
    list_filter = ['room']
    search_fields = ['room', 'fullname']

class ElectricityAdmin(admin.ModelAdmin):
    list_display = ['roomsNumber','old_electricity', 'new_electricity', 'use_electricity']
    list_filter = ['roomsNumber']

    def use_electricity(self, obj):
        return obj.calulate_electricity()
    
admin.site.register(Electricity, ElectricityAdmin)

class HouseAdmin(admin.ModelAdmin):
    list_display = ['nameHouse', 'address']
    list_filter = ['nameHouse']
    search_fields = ['nameHouse']

admin.site.register(House, HouseAdmin)