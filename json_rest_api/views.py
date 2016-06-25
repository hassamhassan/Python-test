from rest_framework import viewsets
from models import Provider, ServiceArea
from serlializer import ProviderSerializer, ServiceAreaSerializer
from django_filters import MethodFilter
from rest_framework import filters


class ProviderViewSet(viewsets.ModelViewSet):
    """
    View set to enable endpoints of Provider
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class ServiceAreaFilter(filters.FilterSet):
    polygon = MethodFilter(action='my_custom_filter')

    class Meta:
        model = ServiceArea
        fields = ['polygon']

    def my_custom_filter(self, queryset, value):
        search_sequence = " ".join(value.split('/'))
        return queryset.filter(
            polygon__contains=search_sequence
        )


class ServiceAreaViewSet(viewsets.ModelViewSet):
    """
    View set to enable endpoints of ServiceArea
    """
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ServiceAreaFilter




