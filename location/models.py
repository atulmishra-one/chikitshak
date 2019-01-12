from django.contrib.gis.db import models as gismodel
from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class State(models.Model):
    name = models.CharField(max_length=60)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=60)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'


class Place(gismodel.Model):
    name = gismodel.CharField(max_length=255)
    geometry = gismodel.PointField()
    country = gismodel.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = gismodel.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = gismodel.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zip_code = gismodel.CharField(max_length=10)

    def __str__(self):
        return self.name

"""
https://maps.googleapis.com/maps/api/geocode/
json?latlng=40.714224,-73.961452&key=AIzaSyBWE-vXoIYTF5HI9dzwwFlB4zA-M7UYZe0
"""
