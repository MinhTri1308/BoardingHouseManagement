from django.db import models

# Create your models here.
class Room(models.Model):
    roomsNumber = models.CharField(max_length=50)
    acreage = models.CharField(max_length=10)
    interior = models.TextField()

    def __str__(self):
        return self.roomsNumber
    