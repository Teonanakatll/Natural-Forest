from django.contrib import admin
from django.utils.safestring import mark_safe

from fire.models import Fire


@admin.register(Fire)
class FireAdmin(admin.ModelAdmin):
    list_display = ('name', 'draft', 'get_video')
    list_display_links = ('name',)
    list_editable = ('draft',)
    readonly_fields = ('get_video',)

    def get_video(self, object):
        if object.video:
            return mark_safe(f"<video src='{object.video.url}' autoplay loop muted width=250>")

    get_video.short_description = 'Текущее видео'
