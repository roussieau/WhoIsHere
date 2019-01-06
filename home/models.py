from django.db import models
from django.utils import timezone

class People(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='home/photos/')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class IP(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, default=None)
    ip = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'
        ordering = ['people']

    def __str__(self):
        return self.ip


class OnlineLog(models.Model):
    date = models.DateTimeField(default=timezone.now)
    is_online = models.BooleanField(default=False)
    people = models.ForeignKey(People, on_delete=models.PROTECT, default=None)

    class Meta:
        verbose_name = 'Online Log'
        verbose_name_plural = 'Online Logs'
        ordering = ['-date', 'people']

    def __str__(self):
        return '{} at {}'.format(self.people, self.date)
