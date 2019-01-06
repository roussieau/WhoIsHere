from home.models import People, IP, OnlineLog
import os


PATH_TO_PING = '/sbin/ping'
PING_COUNT, PING_TIMEOUT = 3, 3     # in seconds


def add_online_logs():
    """ Add log for each user """
    for people in People.objects.all():
        OnlineLog.objects.create(people=people, is_online=is_people_online(people))

def is_people_online(people):
    """ Check if the given People is connected to the network """
    for ip in IP.objects.filter(people=people):
        if os.system("{} -c {} -W {} {}".format(PATH_TO_PING, PING_COUNT, PING_TIMEOUT, ip.ip)) == 0:
            return True
    return False
