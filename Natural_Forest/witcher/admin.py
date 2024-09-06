from django.contrib import admin
from django.utils.safestring import mark_safe

from witcher.models import Witcher


@admin.register(Witcher)
class WitcherAdmin(admin.ModelAdmin):
    list_display = ('name', 'draft', 'get_src', 'get_layer1', 'get_layer2', 'get_layer3', 'get_layer4')
    list_display_links = ('name',)
    list_editable = ('draft',)
    readonly_fields = ('get_layer1', 'get_layer2', 'get_layer3', 'get_layer4', 'get_src',
                       'size_layer1', 'size_layer2', 'size_layer3', 'size_layer4', 'size_src',
                       'get_color')

    fieldsets = (
        (None, {
            'fields': (('draft', 'name'), ('particles_color', 'get_color'))
        }),
        ('Слои', {
            'fields': (('layer1', 'get_layer1', 'size_layer1'), ('layer2', 'get_layer2', 'size_layer2'),
                       ('layer3', 'get_layer3', 'size_layer3'), ('layer4', 'get_layer4', 'size_layer4'),
                       ('src', 'get_src', 'size_src'))
        }),
    )

    def get_color(self, object):
        if object.particles_color:
            return mark_safe(f'<h1 style="background-color:#{object.particles_color};height:100px;width:100px"></h1>')

    get_color.short_description = 'Текущий цвет частиц'

    def get_layer1(self, object):
        if object.layer1:
            return mark_safe(f"<img src='{object.layer1.url}' width=250 height=auto>")

    get_layer1.short_description = 'Текущее изображение'

    def get_layer2(self, object):
        if object.layer2:
            return mark_safe(f"<img src='{object.layer2.url}' width=250 height=auto>")

    get_layer2.short_description = 'Текущее изображение'


    def get_layer3(self, object):
        if object.layer3:
            return mark_safe(f"<img src='{object.layer3.url}' width=250 height=auto>")

    get_layer3.short_description = 'Текущее изображение'

    def get_layer4(self, object):
        if object.layer4:
            return mark_safe(f"<img src='{object.layer4.url}' width=250 height=auto>")

    get_layer4.short_description = 'Текущее изображение'

    def get_src(self, object):
        if object.src:
            return mark_safe(f"<img src='{object.src.url}' width=250 height=auto>")

    get_src.short_description = 'Текущее изображение'
