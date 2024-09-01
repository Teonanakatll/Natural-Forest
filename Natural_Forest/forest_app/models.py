from PIL import Image
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.safestring import mark_safe


class NaturalForest(models.Model):
    """Класс описывающий модель страницы NaturalForest"""

    logo = models.FileField('Логотип с прозрачным фоном', upload_to='image/natural_forest/logo/', validators=[FileExtensionValidator(['svg',])], blank=True)
    layer1 = models.ImageField('Задний фон', upload_to='image/natural_forest/layer1/', blank=True)
    layer2 = models.ImageField('Центральное изображение', upload_to='image/natural_forest/layer2/', blank=True)
    layer3_string1 = models.CharField('1 строка заголовка', max_length=30, blank=True)
    layer3_string2 = models.CharField('2 строка заголовка', max_length=30, blank=True)
    layer3_description = models.CharField('Описание мелкий текст', max_length=255, blank=True)
    layer3_button = models.CharField('Надпись на кнопке', max_length=15, blank=True)
    layer5 = models.ImageField('Передний план падающие листья', upload_to='image/natural_forest/layer5/', blank=True)
    layer6 = models.ImageField('Передний план капли на камере', upload_to='image/natural_forest/layer6/', blank=True)
    draft = models.BooleanField('Черновик', default=True)
    meta_desc = models.CharField('Мета описание', max_length=255, blank=True)

    def __str__(self):
        return f"{self.layer3_string1} {self.layer3_string2}"

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

    def size_layer5(self):
        im = Image.open(self.layer5)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer5.short_description = 'Размер текущего изображения'

    def size_layer6(self):
        im = Image.open(self.layer6)
        (width, height) = im.size
        return mark_safe(f'<h1 class="h1">width={width}, height={height}</h1>')
    size_layer6.short_description = 'Размер текущего изображения'

    class Meta:
        verbose_name = 'Класс NaturalForest'
        verbose_name_plural = 'Классы NanuralForest'
        ordering = ['id']

