from django.contrib import admin

# Register your models here.
from .models import *

class LocationHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'dataArrivedTime', 'latitude', 'altitude', 'longitude', 'deviceId', 'dataCalculatedTime')

admin.site.register(LocationHistory, LocationHistoryAdmin)
