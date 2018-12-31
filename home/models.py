from django.db import models

class IP(models.Model):
    ip = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')
    ips = models.ForeignKey(IP, on_delete=models.CASCADE)
