from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import math

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def eye_balls_captured(request):
    context = {'sample':LocationHistory.objects.order_by('-dataArrivedTime').first()}
    return render(request, 'eye_capture/eye_balls.html', context)

def average_speed(lat_final, long_final, lat_initial, long_initial, time_final, time_initial):
    return distance(lat_final, long_final, lat_initial, long_initial) / (time_final - time_initial)

def distance(lat_final, long_final, lat_initial, long_initial):
    return 112 * math.sqrt((lat_final - lat_initial)**2, (long_final - long_initial)**2)

def traffic_factor(average_speed):
    return 100/average_speed
