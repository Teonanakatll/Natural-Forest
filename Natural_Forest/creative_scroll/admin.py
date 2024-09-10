from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe

from creative_scroll.models import *


class TextItemInline(admin.TabularInline):
    model = TextItem
    extra = 1

class ImageItemInline(admin.TabularInline):
    model = ImageItem
    extra = 1
    readonly_fields = ('get_image',)
    fields = ('get_image', 'title', 'number', 'draft', 'image')

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=auto height=150>")

    get_image.short_description = 'Текущее изображение'


@admin.register(ImageItem)
class ImageItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery', 'number', 'title', 'draft', 'get_image')
    list_editable = ('number', 'draft')
    list_display_links = ('gallery', 'title')
    readonly_fields = ('get_image',)

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=auto height=150>")

    get_image.short_description = 'Текущее изображение'

@admin.register(TextItem)
class TextItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery', 'number', 'draft', 'header')
    list_display_links = ('gallery', 'header')
    list_editable = ('number', 'draft')

@admin.register(GenericGalleryItem)
class GenericGalleryItemAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'content_type', 'object_id', 'get_number_object', 'get_object_info')
    readonly_fields = ('get_object_info', 'get_number_object')




    def get_object_info(self, object):
        if type(object.content_object) == ImageItem:
            return mark_safe(f"<img src='{object.content_object.image.url}' height=150>")
        return mark_safe(f"<h1 class='h1'>{object.content_object.header}</h1>")

    def get_number_object(self, object):
        return object.content_object.number

    get_number_object.short_description = 'Порядковый номер в галерее'
    get_object_info.short_description = 'Инфо объекта'

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """Классы """
    list_display = ('name', 'get_gallery_images')
    readonly_fields = ('get_gallery_images',)

    inlines = (ImageItemInline, TextItemInline)

    def get_gallery_images(self, object):
        if object.imageitem_set:
            gallery = ''
            lst = object.imageitem_set.all()
            for i in lst:
                gallery += f'<img class="gallery" src="{i.image.url}" height=150>'
            return mark_safe(gallery)

    get_gallery_images.short_description = 'Все изображения галереи'


@admin.register(Canvas)
class CanvasAdmin(admin.ModelAdmin):
    list_display = ('header_h1', 'get_background_image', 'left_gallery', 'right_gallery')
    list_display_links = ('header_h1', )
    readonly_fields = ('get_background_image',)


    def get_background_image(self, object):
        if object.background_image:
            return mark_safe(f"<img src='{object.background_image.url}' width=auto height=150>")

    get_background_image.short_description = 'Текущее изображение'




