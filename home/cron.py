from home.models import People, IP, OnlineLog, MacAddress
import os, subprocess


LAN = '192.168.1.0/24'
PATH_TO_PING = '/sbin/ping'
PING_COUNT, PING_TIMEOUT = 3, 3     # in seconds


def add_online_logs():
    """ Add log for each user """
    output = str(subprocess.check_output('/usr/local/bin/nmap -sn {}'.format(LAN), shell=True)).upper()
    for people in People.objects.all():
        OnlineLog.objects.create(people=people, is_online=is_people_online(people, output))

def is_people_online(people, nmap):
    """ Check if the given People is connected to the network through MAC or IP Address """
    for mac_address in MacAddress.objects.filter(people=people):
        if mac_address.mac_address in nmap:
            return True

    for ip in IP.objects.filter(people=people):
        if ip.ip in nmap:
            return True
    return False
