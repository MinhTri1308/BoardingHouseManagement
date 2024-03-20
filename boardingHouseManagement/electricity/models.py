from django.db import models
from room.models import Room
# Create your models here.
class Electricity(models.Model):
    roomsNumber = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    old_electricity = models.IntegerField()
    new_electricity = models.IntegerField()

    def calulate_electricity(self):
        return self.new_electricity - self.old_electricity
    
    #override method save() in models.Model is django
    def save(self, *args, **kwargs):
        self.use_electricity = self.calulate_electricity()
        super(Electricity, self).save(*args, **kwargs)