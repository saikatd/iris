from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from services.location_service import *
import math

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def eyes_captured(request):
    drivers = Driver.objects.all()
    driver_sessions = {}
    for driver in drivers:
        driver_sessions[driver] = driver_session(driver.id)
    context = {'driver_sessions' : driver_sessions}
    return render(request, 'eye_capture/eyes.html', context)

def driver_eyes_captured(request, driver_id):
    context = { 'sessions' : driver_session(driver_id)}
    return render(request, 'eye_capture/driver_eyes.html', context)

def driver_session(driver_id):
    locations = LocationHistory.objects.filter(userId=driver_id).order_by('-dataArrivedTime')
    sessions = []
    if locations.count() < 2:
        return sessions
    previous_location = locations[0]
    eyes_per_session = 0
    for i in range(1, len(locations)):
        delta_time = abs(locations[i].dataArrivedTime - previous_location.dataArrivedTime).total_seconds() / 60
        loc_final = Point(locations[i].latitude, locations[i].longitude)
        loc_initial = Point(previous_location.latitude, previous_location.longitude)
        dist = GeoCalculator.distance(loc_final, loc_initial)
        print "delta_time: " + str(delta_time) + " distance: " + str(dist)
        if SessionBreakPoint.is_session_breakpoint(delta_time, dist):
            eye_ball = Traffic.eyes(loc_final, loc_initial, delta_time)
            eyes_per_session += eye_ball
        else:
            if eyes_per_session != 0:
                print "eyes_per_session: " + str(eyes_per_session)
                print
                sessions.append(eyes_per_session)
                eyes_per_session = 0

        previous_location = locations[i]
    sessions.append(eyes_per_session)
    return sessions
