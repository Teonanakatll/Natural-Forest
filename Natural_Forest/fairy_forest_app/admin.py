from django.contrib import admin
from django.utils.safestring import mark_safe

from fairy_forest_app.models import FairyForest


@admin.register(FairyForest)
class FairyForestAdmin(admin.ModelAdmin):
    list_display = ('get_header', 'draft', 'get_layer1', 'get_layer3', 'get_layer4', 'get_footer_decor', 'get_footer_bg')
    list_display_links = ('get_header',)
    readonly_fields = ('get_header', 'get_layer1', 'get_layer3', 'get_layer4', 'get_footer_decor', 'get_footer_bg',
                       'size_layer1', 'size_layer3', 'size_layer4', 'size_footer_decor', 'size_footer_bg')
    list_editable = ('draft',)
    save_as = True


    fieldsets = (
        ('Слои верхнего экрана', {
            'fields': (('layer1', 'get_layer1', 'size_layer1'), ('layer2_header',), ('layer2_title',),
                       ('layer3', 'get_layer3', 'size_layer3'), ('layer4', 'get_layer4', 'size_layer4'))
        }),
        ('Слои нижнего экрана, черновик и копирайт', {
            'fields': (('footer_decor', 'get_footer_decor', 'size_footer_decor'), ('footer_bg', 'get_footer_bg', 'size_footer_bg'),
                       ('footer_header',), ('footer_text',),('copy',), ('draft',))
        }),
    )

    def get_header(self, object):
        if object.layer2_header and object.layer2_title:
            return mark_safe(f'<h1 class="h1">{object.layer2_header} {object.layer2_title}</h1>')

    def get_layer1(self, object):
        if object.layer1:
            return mark_safe(f"<img src='{object.layer1.url}' width=250 height=auto>")

    get_layer1.short_description = 'Текущее изображение'

    def get_layer3(self, object):
        if object.layer3:
            return mark_safe(f"<img src='{object.layer3.url}' width=250 height=auto>")

    get_layer3.short_description = 'Текущее изображение'

    def get_layer4(self, object):
        if object.layer4:
            return mark_safe(f"<img src='{object.layer4.url}' width=250 height=auto>")

    get_layer4.short_description = 'Текущее изображение'

    def get_footer_decor(self, object):
        if object.footer_decor:
            return mark_safe(f"<img src='{object.footer_decor.url}' width=250 height=auto>")

    get_footer_decor.short_description = 'Текущее изображение'

    def get_footer_bg(self, object):
        if object.footer_bg:
            return mark_safe(f"<img src='{object.footer_bg.url}' width=250 height=auto>")

    get_footer_bg.short_description = 'Текущее изображение'

