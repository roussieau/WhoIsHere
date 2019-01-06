from django.shortcuts import render
from .models import People, IP, OnlineLog
import os

def index(request):
    return render(request, 'home/index.html', {'peoples_status': get_status()})


def get_status():
    """ Return the status of the every People in the database """
    return [{'name': people.name,
            'photo': people.photo,
            'is_online': is_people_online(people)}
        for people in People.objects.all()]

def is_people_online(people):
    """ Return the last log concering the given People """
    people_logs = OnlineLog.objects.filter(people=people)
    return people_logs.first().is_online if len(people_logs) != 0 else False
