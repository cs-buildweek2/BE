from django.db import models
# Create your models here.

class Rooms(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    room_id = models.IntegerField()
    title = models.TextField(max_length=40)
    description = models.TextField(max_length=300)
    coordinates = models.CharField(max_length=40)

class Exits(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    direction = models.TextField(blank=True)
    direction_id = models.IntegerField()