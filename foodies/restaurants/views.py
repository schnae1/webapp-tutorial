#from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Restaurants
from django.contrib.gis.geos import Point

longitude = -115.063427
latitude = 36.100423

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Restaurants
    context_object_name = 'restaurants'
    queryset = Restaurants.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:20]
    template_name = 'restaurants/index.html'
    

home = Home.as_view()
