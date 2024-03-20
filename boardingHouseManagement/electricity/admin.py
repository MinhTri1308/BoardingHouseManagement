from django.contrib import admin
from .models import Electricity
# Register your models here.
class ElectricityAdmin(admin.ModelAdmin):
    list_display = ['roomsNumber','old_electricity', 'new_electricity', 'use_electricity']
    list_filter = ['roomsNumber']

    def use_electricity(self, obj):
        return obj.calulate_electricity()
    


admin.site.register(Electricity, ElectricityAdmin)