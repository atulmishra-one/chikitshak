from rest_framework import routers
from location.viewsets import StateApiView
from location.viewsets import CityApiView

router = routers.DefaultRouter()
router.register(r'state', StateApiView, base_name="state")
router.register(r'city', CityApiView, base_name="city")
