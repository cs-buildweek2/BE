from django.db import models
import uuid
# Create your models here.

class Rooms(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.IntegerField()
    coordinates = models.CharField(max_length=40)

class Exits(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    room_id = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    direction = models.TextField()
    direction_id = models.IntegerField()