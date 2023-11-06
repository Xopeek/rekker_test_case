from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from personal_feed.models import Achievement


class UserAchievement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Получил ачивку'
    )
    achievement = models.ForeignKey(
        Achievement,
        on_delete=models.CASCADE,
        verbose_name='Ачивка'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата получения'
    )

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Ачивка пользователя'
        verbose_name_plural = 'Ачивки пользователей'

    def __str__(self):
        return f'{self.user} -> {self.achievement}'


class User(AbstractUser):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=settings.MAX_LENGTH_FIRST_NAME,
        blank=False
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=settings.MAX_LENGTH_LAST_NAME,
        blank=False
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='UserAchievement',
        related_name='users',
        blank=True,
        verbose_name='Ачивки'
    )

    class Meta:
        ordering = ('first_name', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
