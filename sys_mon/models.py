from django.db import models

# Create your models here.
class Device(models.Model):
    svr_name = models.CharField(max_length=200)
    content = models.TextField(null = True)

class Fan(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    fan_name = models.CharField(max_length=200)
    fan_status = models.CharField(max_length=200)
    fan_health = models.CharField(max_length=200)
    created_time = models.DateTimeField(null = True)