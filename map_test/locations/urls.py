from django.urls import path

from map_test.locations.views import index

urlpatterns = [
    path('', index, name='index'),
]