from django.apps import AppConfig


class CreativeScrollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'creative_scroll'

    def ready(self):
        import creative_scroll.signals
