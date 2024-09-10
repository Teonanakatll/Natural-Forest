from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save


# переопределяем мереджер обьектов
class ActiveManager(models.Manager):
    def no_draft(self):
        return super().get_queryset().filter(draft=False)


class Gallery(models.Model):
    name = models.CharField('Название', max_length=20)

    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Название галереи', blank=True)
    title = models.CharField('Название', max_length=200, blank=True)
    number = models.PositiveSmallIntegerField('Порядковый номер')
    draft = models.BooleanField('Черновик', default=True)

    # кастомный менеджер
    # objects = ActiveManager()

    def __str__(self):
        if self.title:
            return self.title
        return self.pk

    class Meta:
        abstract = True


class ImageItem(GalleryItem):
    image = models.ImageField('Изображение', upload_to='images/creative_scroll/')

    class Meta:
        verbose_name = 'Фото айтем'
        verbose_name_plural = 'Фото айтемы'


class TextItem(GalleryItem):
    header = models.CharField('Заголовок', max_length=255, blank=True)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return f"{self.gallery.name} - {self.header}"

    class Meta:
        verbose_name = 'Текстовый айтем'
        verbose_name_plural = 'Текстовые айтемы'


class GenericGalleryItem(models.Model):
    ITEM_CHOICES = {
        ImageItem: 'Фото айтем',
        TextItem: 'Текстовый айтем'
    }

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, verbose_name='Галерея')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name='Тип айтема',
                                     limit_choices_to={
                                         'model__in': ['imageitem', 'textitem']
                                     })
    object_id = models.PositiveSmallIntegerField()
    # через это поле можно обращаться к полям связанных моделей (ImageItem или TextItem)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['id']
        verbose_name = 'Связь айтема с галереей'
        verbose_name_plural = 'Связь айтемов с галерей'


class Canvas(models.Model):
    background = models.CharField('Цвет в формате RGB', max_length=7, default='#1D1D1D')
    background_image = models.ImageField('Главное изображение', upload_to='image/creative_scroll/bg_img/')
    header_h1 = models.CharField('Заголовок сайта', max_length=30, blank=True)
    left_gallery = models.ForeignKey(Gallery, on_delete=models.DO_NOTHING, verbose_name='Левая галерея', related_name='canvas')
    right_gallery = models.ForeignKey(Gallery, on_delete=models.DO_NOTHING, verbose_name='Правая галерея', related_name='canvas1')

    class Meta:
        verbose_name = 'Главный класс сайта'
        verbose_name_plural = 'Главные классы сайта'
        ordering = ['id']

    def __str__(self):
        return self.header_h1

# def image_item_post_save(sender, instance, created, **kwargs):
#     content_type = ContentType.objects.get_for_model(ImageItem)
#
#     GenericGalleryItem.objects.update_or_create(
#         content_type=content_type,
#         object_id=instance.id,
#         defaults={'gallery': instance.gallery}
#     )
#
# post_save.connect(image_item_post_save, sender=ImageItem)