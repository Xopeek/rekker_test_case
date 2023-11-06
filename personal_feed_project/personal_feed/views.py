from rest_framework import filters, generics

from personal_feed.filters import UserFeedFilter
from personal_feed.models import Advertisement, Note
from personal_feed.pagination import UserFeedPagination
from personal_feed.serializers import (AdvertisementSerializer, NoteSerializer,
                                       UserAchievementSerializer)
from users.models import UserAchievement


class UserFeedView(generics.ListAPIView):
    """
        User Feed View

        Parameters:
        - `search` (str): A search query to filter results by title.

        Response:
        - List of events with pagination support.
    """
    serializer_class = None
    pagination_class = UserFeedPagination
    filter_backends = [filters.SearchFilter]
    filterset_class = UserFeedFilter
    search_fields = ['title']

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user_notes = Note.objects.filter(
            author_id=user_id
        ).order_by('-created_at')
        user_achievements = UserAchievement.objects.filter(
            user_id=user_id
        ).order_by('-created_at')
        advertisements = Advertisement.objects.order_by('-created_at')

        queryset = []

        for note in user_notes:
            queryset.append({
                'type': f'Пользователь написал заметку <{note.title}>',
                'data': NoteSerializer(note).data
            })

        for user_achievement in user_achievements:
            queryset.append({
                'type': f'Пользователь получил достижение'
                        f' <{user_achievement.achievement.name}>',
                'data': UserAchievementSerializer(user_achievement).data
            })

        for ad in advertisements:
            queryset.append({
                'type': 'Рекламное объявление.',
                'data': AdvertisementSerializer(ad).data
            })

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        search_query = self.request.query_params.get('search', '')
        if search_query:
            queryset = [
                item for item in queryset if search_query in item.get(
                    'data', {}
                ).get('title', '')
            ]

        sorted_events = sorted(
            queryset, key=lambda event: event['data']['created_at'],
            reverse=True
        )

        page = self.paginate_queryset(sorted_events)
        return self.get_paginated_response(page)
