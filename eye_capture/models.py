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
