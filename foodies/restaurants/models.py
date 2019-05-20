#from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class Restaurants(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Restaurants"
