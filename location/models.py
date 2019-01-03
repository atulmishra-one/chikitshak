from django.contrib.gis.db import models


# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=255)
    geometry = models.PointField()
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


"""
https://maps.googleapis.com/maps/api/geocode/
json?latlng=40.714224,-73.961452&key=AIzaSyBWE-vXoIYTF5HI9dzwwFlB4zA-M7UYZe0
"""
