from django.shortcuts import render
import folium
import geocoder

# Create your views here.
from map_test.locations.forms import LocationForm
from map_test.locations.models import Location


def index(request):
    initial_location = [42.621834, 25.395756]
    initial_zoom = 7
    m = folium.Map(location=initial_location, zoom_start=initial_zoom)
    locations = Location.objects.all()
    for loc in locations:
        location = geocoder.osm(loc.address)
        location_popup = ', '.join([location.location, location.country, str(loc.date_added.date())])
        folium.Marker([location.lat, location.lng], tooltip='Click for details',
                      popup=location_popup).add_to(m)

    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            new_address = form.cleaned_data['address']
            form.save()
            address = geocoder.osm(new_address)
            new_lat_lng = (address.lat, address.lng)
            folium.Marker(new_lat_lng, tooltip='Click for details',
                          popup=', '.join([address.location, address.country])).add_to(m)
    else:
        form = LocationForm()

    m = m._repr_html_

    context = {
        'map': m,
        'form': form
    }

    return render(request, 'index.html', context=context)
