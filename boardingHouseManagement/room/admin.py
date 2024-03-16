from django.contrib import admin
from .models import Room
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ['roomsNumber', 'acreage']
    list_filter = ['acreage']
    search_fields = ['roomsNumber', 'acreage']


admin.site.register(Room, RoomAdmin)