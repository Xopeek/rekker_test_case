import django_filters
from django.db.models import Q

from personal_feed.models import Note


class UserFeedFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        method='filter_title',
        label='Title Search'
    )

    class Meta:
        model = Note
        fields = ['title']

    def filter_title(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value)
            | Q(advertisement__title__icontains=value)
        )
