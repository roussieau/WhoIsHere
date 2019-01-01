from django.db import models

class People(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures')

class IP(models.Model):
    people = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
