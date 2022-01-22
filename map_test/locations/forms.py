from django import forms
import geocoder
from django.core.exceptions import ValidationError

from map_test.locations.models import Location


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('address',)


    def clean_address(self):
        address = self.cleaned_data['address']
        valid_address = geocoder.osm(address)
        print(address)
        if not valid_address:
            raise ValidationError('No such address! Enter a valid one!')

        return address