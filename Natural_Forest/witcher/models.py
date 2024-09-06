from PIL import Image
from django.db import models
from django.utils.safestring import mark_safe


class Witcher(models.Model):
    """Класс аписывает модель горизонтального параллакс слайдера"""
    name = models.CharField('Название', max_length=40, blank=True)
    layer1 = models.ImageField('Задний фон', upload_to='images/witcher/layer1', blank=True)
    layer2 = models.ImageField('Средний дальний план', upload_to='images/witcher/layer2', blank=True)
    layer3 = models.ImageField('Средний ближний план', upload_to='images/witcher/layer3', blank=True)
    layer4 = models.ImageField('Передний план', upload_to='images/witcher/layer4', blank=True)
    src = models.ImageField('Исходник', upload_to='images/witcher/src', blank=True)
    particles_color = models.CharField('Цвет частиц', max_length=6, blank=True)
    draft = models.BooleanField('Черновик', default=True)

    class Meta:
        verbose_name = 'Класс Witcher'
        verbose_name_plural = 'Классы Witcher'

    def __str__(self):
        return self.name

    def size_layer1(self):
        im = Image.open(self.layer1)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer1.short_description = 'Размер текущего изображения'

    def size_layer2(self):
        im = Image.open(self.layer2)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer2.short_description = 'Размер текущего изображения'

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

    def size_src(self):
        im = Image.open(self.src)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_src.short_description = 'Размер исходника'