from django.core.validators import FileExtensionValidator
from django.db import models

class Fire(models.Model):
    """Описывает класс Fire"""
    name = models.CharField('Название', max_length=200, blank=True)
    video = models.FileField('Видео', upload_to='video/fire', validators=[FileExtensionValidator(['mp4', 'gif', 'mpeg-4', 'mov', 'avi', 'webm'])])
    draft = models.BooleanField('Черновик', default=True)

    class Meta:
        verbose_name = 'Класс Fire'
        verbose_name_plural = 'Классы Fire'

    def __str__(self):
        return self.name
