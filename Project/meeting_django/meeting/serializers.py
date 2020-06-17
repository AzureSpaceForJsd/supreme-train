from rest_framework import serializers
from .models import MeetingRoom

class MeetingRoomsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MeetingRoom
        fields = '__all__'
