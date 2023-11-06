from django.conf import settings
from django.db import models


class Note(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=settings.MAX_LENGTH_NOTE_TITLE
    )
    body = models.TextField(
        verbose_name='Тело'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='note'
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title


class Achievement(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=settings.MAX_LENGTH_ACHIEVEMENT_NAME
    )
    condition = models.TextField(
        'Условие получения'
    )
    icon = models.ImageField(
        upload_to='achievements/'
    )

    class Meta:
        verbose_name = 'Ачивка'
        verbose_name_plural = 'Ачивки'

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=settings.MAX_LENGTH_ADVERTISEMENT_TITLE
    )
    description = models.TextField(
        'Описание'
    )
    image = models.ImageField(
        upload_to='advertisements/'
    )
    link = models.URLField()
    created_at = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Рекламное объявление'
        verbose_name_plural = 'Рекламные объявления'

    def __str__(self):
        return self.title
