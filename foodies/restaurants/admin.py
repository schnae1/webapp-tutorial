from django.contrib import admin

# Register your models here.

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Restaurants

@admin.register(Restaurants)
class RestaurantsAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
