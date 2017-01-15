from __future__ import unicode_literals

from django.db import models

# Create your models here.
class LocationHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    dataArrivedTime = models.DateTimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    altitude = models.DecimalField(max_digits=15, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    deviceId = models.CharField(max_length=200)
    dataCalculatedTime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'traceper_user_was_here'


class Driver(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=32)
    group = models.IntegerField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)
    altitude = models.DecimalField(max_digits=15, decimal_places=6)
    realname = models.CharField(max_length=80)
    email = models.CharField(max_length=100)
    dataArrivedTime = models.DateTimeField()
    deviceId = models.CharField(max_length=200)
    status_message = models.CharField(max_length=128)
    status_source = models.IntegerField()
    status_message_time = models.DateTimeField()
    dataCalculatedTime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'traceper_users'
