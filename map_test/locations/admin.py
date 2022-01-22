from django.contrib import admin

# Register your models here.
from map_test.locations.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass