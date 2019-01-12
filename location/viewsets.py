from rest_framework import viewsets
from location.models import State
from location.models import City
from location.serializers import StateSerializer


class StateApiView(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

    def get_queryset(self):
        country_id = self.request.query_params.get("country_id", None)
        if country_id:
            queryset = State.objects.filter(country=country_id)
        else:
            queryset = State.objects.all()
        return queryset


class CityApiView(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = City.objects.all()

    def get_queryset(self):
        state_id = self.request.query_params.get("state_id", None)
        if state_id:
            queryset = City.objects.filter(state=state_id)
        else:
            queryset = City.objects.all()
        return queryset



