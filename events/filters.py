import django_filters

from .models import Event


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    location = django_filters.CharFilter(lookup_expr="icontains")
    organizer = django_filters.NumberFilter(field_name="organizer__id")
    date = django_filters.DateFilter(field_name="date__date")
    date_from = django_filters.DateTimeFilter(field_name="date", lookup_expr="gte")
    date_to = django_filters.DateTimeFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Event
        fields = ["title", "location", "organizer", "date", "date_from", "date_to"]
