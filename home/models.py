from django.db import models


class People(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='home/photos/')

    def __str__(self):
        return self.name


class IP(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE, default=None)
    ip = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'

    def __str__(self):
        return self.ip
