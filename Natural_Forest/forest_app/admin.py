from django.contrib import admin
from django.utils.safestring import mark_safe

from forest_app.models import NaturalForest


@admin.register(NaturalForest)
class NaturalForestAdmin(admin.ModelAdmin):
    """Описывает представление модели в админке"""
    list_display = ('get_header', 'draft', 'get_logo', 'get_layer1', 'get_layer2', 'get_layer5', 'get_layer6')
    list_display_links = ('get_header',)
    readonly_fields = ('get_header', 'get_layer1', 'get_layer2', 'get_layer5', 'get_layer6', 'get_logo',
                       'size_layer1', 'size_layer2', 'size_layer5', 'size_layer6')
    list_editable = ('draft',)

    fieldsets = (
        ('Логотип, задний фон, layer2', {
            'fields': (('logo', 'get_logo'), ('layer1', 'get_layer1', 'size_layer1'), ('layer2', 'get_layer2', 'size_layer2'))
        }),
        ('Текстовая информация среднего плана: заголовок, описание и кнопка', {
            'fields': (('layer3_string1', 'layer3_string2'), ('layer3_description', 'layer3_button'))
        }),
        ('Передний план: например падающие листья и капли на обьективе', {
            'fields': (('layer5', 'get_layer5', 'size_layer5'), ('layer6', 'get_layer6', 'size_layer6'))
        }),
        ('Мета описание, черновик', {
            'fields': (('meta_desc',),('draft',))
        })
    )

    def get_layer1(self, object):
        if object.layer1:
            return mark_safe(f"<img src='{object.layer1.url}' width=250 height=auto>")

    get_layer1.short_description = 'Фото заднего фона'

    def get_logo(self, object):
        if object.logo:
            return mark_safe(f"<img src='{object.logo.url}' style='background-color: #263238' width=100 height=auto>")

    get_logo.short_description = 'Текущее изображение'

    def get_header(self, object):
        if object.layer3_string1 and object.layer3_string2:
            return mark_safe(f"<h1>{object.layer3_string1} {object.layer3_string2}</h1>")

    def get_layer2(self, object):
        if object.layer2:
            return mark_safe(f"<img src='{object.layer2.url}' width=250 height=auto>")

    get_layer2.short_description = 'Текущее изображение'

    def get_layer5(self, object):
        if object.layer5:
            return mark_safe(f"<img src='{object.layer5.url}' style='background-color: #263238' width=250 height=auto>")

    get_layer5.short_description = 'Текущее изображение'

    def get_layer6(self, object):
        if object.layer6:
            return mark_safe(f"<img src='{object.layer6.url}' style='background-color: #263238' width=250 height=auto>")

    get_layer6.short_description = 'Текущее изображение'
