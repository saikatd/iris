from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import math

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def eye_balls_captured(request):
    driver = Driver.objects.get(email='adhitms@gmail.com')
    locations = LocationHistory.objects.filter(userId=driver.id).order_by('-dataArrivedTime')
    sessions = []
    previous_location = locations[0]
    eye_balls_per_session = 0
    for i in range(1, len(locations)):
        delta_time = (locations[i].dataArrivedTime - previous_location.dataArrivedTime).total_seconds() / 60
        dist = distance(locations[i].latitude, previous_location.latitude,
                        locations[i].longitude, previous_location.longitude)
        if delta_time <= 20 and dist >= 100:
            eye_ball = eye_balls(locations[i].latitude, previous_location.latitude,
                                    locations[i].longitude, previous_location.longitude,
                                    delta_time)
            eye_balls_per_session += eye_ball
            print eye_balls_per_session
        else:
            sessions.append(eye_balls_per_session)
    sessions.append(eye_balls_per_session)
    print sessions
    context = {'sessions' : sessions}
    return render(request, 'eye_capture/eye_balls.html', context)

def eye_balls(lat_final, long_final, lat_initial, long_initial, delta_time):
    return 100/average_speed(lat_final, long_final, lat_initial, long_initial, delta_time)

def average_speed(lat_final, long_final, lat_initial, long_initial, delta_time):
    return distance(lat_final, long_final, lat_initial, long_initial) / delta_time

def distance(lat_final, long_final, lat_initial, long_initial):
    squared_distance = float((lat_final - lat_initial)**2 + (long_final - long_initial)**2)
    return 112 * math.sqrt(squared_distance)

def traffic_factor(average_speed):
    return 100/average_speed
