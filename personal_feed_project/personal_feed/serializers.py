from rest_framework import serializers

from personal_feed.models import Achievement, Advertisement, Note
from users.models import UserAchievement


class NoteSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = (
            'title',
            'body',
            'created_at',
            'author_name'
        )

    def get_author_name(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            'name',
            'condition',
            'icon'
        )


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = (
            'title',
            'description',
            'image',
            'link',
            'created_at'
        )


class UserAchievementSerializer(serializers.ModelSerializer):
    achievement = AchievementSerializer()

    class Meta:
        model = UserAchievement
        fields = (
            'achievement',
            'created_at'
        )
