# This file connects model to REST framework
from rest_framework import serializers, viewsets
from .models import Rooms

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Rooms #tells us which model we are using
        fields = ('room_id','coordinates') #tells us which fields from that model we want to use

class RoomsViewSet(viewsets.ModelViewSet): #tells us rows were interested in showing
    serializer_class = RoomSerializer #connects this class with RoomSerializer class
    queryset = Rooms.objects.all() #tells us which things we want to return