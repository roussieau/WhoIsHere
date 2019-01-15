from django.core.management.base import BaseCommand, CommandError
from home.models import People, OnlineLog, MacAddress


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('arp_scan', type=str)

    def handle(self, *args, **options):
        """ Add Logs to the database indicating who is connected to the network """
        arp_scan = options['arp_scan'].upper()
        for people in People.objects.all():
            OnlineLog.objects.create(people=people, is_online=self.is_people_online(people, arp_scan))

    def is_people_online(self, people, arp_scan):
        """ Check if the given People is connected to the network through MAC or IP Address """
        for mac_address in MacAddress.objects.filter(people=people):
            if mac_address.mac_address in arp_scan:
                return True
        return False
