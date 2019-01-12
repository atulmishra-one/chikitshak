from django.contrib import admin
from location.models import Place
from location.models import Country
from location.models import State
from location.models import City
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldInlineWidget
from location.forms import AdminPlaceFormExtra
# Register your models here.


class PlaceAdmin(admin.ModelAdmin):
    form = AdminPlaceFormExtra
    list_display = ("name", "country", "state", "city", "zip_code", "geometry")
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldInlineWidget}
    }

    class Media:
        js = ("https://cdn.jsdelivr.net/npm/vue/dist/vue.js",
              "https://unpkg.com/axios/dist/axios.min.js",
              "https://cdn.jsdelivr.net/npm/lodash@4.13.1/lodash.min.js", )


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'country')

    @classmethod
    def country(cls, obj):
        return obj.state.country


admin.site.register(Country)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Place, PlaceAdmin)


