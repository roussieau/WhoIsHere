from django.shortcuts import render
from home.models import People, IP
import os

def home(request):
    return render(request, 'home/home.html', scan())

def scan():
    states = []
    for people in People.objects.all().order_by('-name'):
        states.append( {'name' : people.name,
                        'picture': people.picture,
                        'is_online': is_people_online(people)} )
    return states

def is_people_online(people):
    for ip in IP.objects.filter(people=people):
        if os.system("ping -o -c 3 -W 3000 {}".format(ip)) != 0:
            return True
    return False
