from django.forms import ModelForm
from django import forms
from location.models import Place, State, City


class StateWidget(forms.Select):
    template_name = "location/forms/widgets/state.html"


class AdminPlaceForm(ModelForm):

    class Meta:
        model = Place
        fields = ('name', 'geometry', 'country', 'state', 'city', 'zip_code')
        widgets = {
            "state": StateWidget()
        }


class AdminPlaceFormExtra(AdminPlaceForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['state'].queryset = State.objects.none()
        self.fields['city'].queryset = City.objects.none()

        if self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')
            self.fields['city'].queryset = self.instance.state.city_set.order_by('name')

    class Media:
        js = ("admin_place_form.js", )


