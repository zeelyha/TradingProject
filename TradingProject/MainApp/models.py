from django.db import models

# Create your models here.
class File(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    date = models.IntegerField()
    time = models.TimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.CharField(max_length=20)