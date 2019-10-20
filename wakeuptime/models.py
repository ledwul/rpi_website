from django.db import models

# Create your models here.
class WakeUpTime(models.Model):
    time_sec = models.IntegerField(default=0)

