from PIL import Image
from django.db import models
from django.utils.safestring import mark_safe


class FairyForest(models.Model):
    """Класс описывает донные модели FairyForest"""

    layer1 = models.ImageField('Задний план', upload_to='image/fairy_forest/layer1/', blank=True)
    layer2_header = models.CharField('Задний план крупный заголовок', max_length=20, blank=True)
    layer2_title = models.CharField('Задний план мелкий заголовок', max_length=40, blank=True)
    layer3 = models.ImageField('Средний план', upload_to='image/fairy_forest/layer3/', blank=True)
    layer4 = models.ImageField('Передний план', upload_to='image/fairy_forest/layer4/', blank=True)
    footer_decor = models.ImageField('Декор между экранами', upload_to='image/fairy_forest/footer_decor/', blank=True)
    footer_bg = models.ImageField('Фон футера', upload_to='image/fairy_forest/footer_bg/')
    footer_header = models.CharField('Заголовок футера', max_length=40, blank=True)
    footer_text = models.TextField('Текст футера', blank=True)
    copy = models.CharField('Копирайт', max_length=255, blank=True)
    draft = models.BooleanField('Черновик', default=True)

    def __str__(self):
        return f'{self.layer2_header} {self.layer2_title}'

    def size_layer1(self):
        im = Image.open(self.layer1)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer1.short_description = 'Размер текущего изображения'

    def size_layer3(self):
        im = Image.open(self.layer3)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer3.short_description = 'Размер текущего изображения'

    def size_layer4(self):
        im = Image.open(self.layer4)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer4.short_description = 'Размер текущего изображения'

    def size_footer_decor(self):
        im = Image.open(self.footer_decor)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_footer_decor.short_description = 'Размер текущего изображения'

    def size_footer_bg(self):
        im = Image.open(self.footer_bg)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_footer_bg.short_description = 'Размер текущего изображения'


    class Meta:
        verbose_name = 'Класс FairyForest'
        verbose_name_plural = 'Классы FairyForest'


