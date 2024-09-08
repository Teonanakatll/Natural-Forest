from django.urls import path

from fire.views import fire

urlpatterns = [
    path('fire/', fire, name='fire')
]