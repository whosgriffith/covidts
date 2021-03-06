# Local imports
import django_filters
from .models import Ubication

class UbicationFilter(django_filters.FilterSet):
    class Meta:
        model = Ubication
        fields = {
            'id': ['exact'],
            'city': ['icontains'],
            'province': ['icontains'],
            'poblation': ['icontains'],
        }