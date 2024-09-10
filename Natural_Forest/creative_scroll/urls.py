from django.urls import path

from creative_scroll.views import creative_scroll

urlpatterns = [
    path('creative_scroll', creative_scroll, name='creative_scroll')
]