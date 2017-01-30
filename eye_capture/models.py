from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class LocationHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    driver = models.ForeignKey('Driver', null=True, db_column='userId')
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
    campaign = models.ForeignKey('Campaign', null=True, db_column='group')
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

class Campaign(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    owner = models.ForeignKey('CampaignOwner', null=True, db_column='owner')
    description = models.CharField(max_length=500)
    startsAt = models.DateTimeField(default=datetime.now, blank=True)
    endsAt = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        managed = True
        db_table = 'traceper_groups'


class CampaignOwner(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=500)

    class Meta:
        managed = True
        db_table = 'traceper_campaign_owners'
