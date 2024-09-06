from django.urls import path

from witcher.views import witcher

urlpatterns = [
    path('witcher/', witcher, name='witcher')
]