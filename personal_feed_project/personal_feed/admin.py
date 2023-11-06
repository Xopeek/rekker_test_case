from django.contrib import admin

from personal_feed.models import Achievement, Advertisement, Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'created_at',
        'author'
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'condition'
    )


@admin.register(Advertisement)
class Advertisement(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'link',
        'created_at'
    )
