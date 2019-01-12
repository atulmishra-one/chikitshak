from django.urls import path
from django.urls import include
from location.routers import router

urlpatterns = [
    path("api/", include(router.urls))
]
