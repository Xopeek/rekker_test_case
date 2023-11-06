from django.contrib import admin

from users.models import User, UserAchievement


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'
    )


@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'achievement'
    )
