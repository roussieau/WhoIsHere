from django.contrib import admin
from home import models

admin.site.register(models.People)
admin.site.register(models.IP)
admin.site.register(models.MacAddress)
