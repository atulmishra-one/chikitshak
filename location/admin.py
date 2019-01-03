from django.contrib import admin
from location.models import Place
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldInlineWidget
# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "zip_code", "geometry")
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldInlineWidget}
    }


admin.site.register(Place, PlaceAdmin)

