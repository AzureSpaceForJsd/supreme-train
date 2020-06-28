from django.db import models

# Create your models here.

class MeetingRoom(models.Model):
    roomNo = models.CharField(max_length=10)
    roomName = models.CharField(max_length=50)
    roomAddr = models.CharField(max_length=256)
    roomSts = models.CharField(max_length=1)
    roomLevel = models.CharField(max_length=10)
    roomMedia = models.CharField(max_length=20)
    class Room:
        db_table = 'Room'
        objects = models.Manager()

class Reserve(models.Model):
    reservDate = models.DateField()
    reserveStartTime = models.TimeField()
    reserveEndTime = models.TimeField()
    mediaFlg = models.CharField(max_length=1)
    reservePerson = models.CharField(max_length=50)
    class ReserveRoom:
        db_table = 'ReserveRoom'
        objects = models.Manager()