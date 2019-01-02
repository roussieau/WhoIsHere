from django.shortcuts import render
from .models import People, IP
import os

def index(request):
    return render(request, 'home/index.html', {'peoples_status': get_status()})


def get_status():
    """ Return the status of the every People in the database """
    return [{'name': people.name,
            'photo': people.photo,
            'is_online': is_people_online(people)}
        for people in People.objects.all().order_by('-name')]

def is_people_online(people):
    """ Check if the given People is connected to the network """
    for ip in IP.objects.filter(people=people):
        if os.system("ping -o -c 3 -W 3000 {}".format(ip.ip)) == 0:
            return True
    return False
