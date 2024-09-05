from django.urls import path

from forest_app.views import forest, index

urlpatterns = [
    path('', index, name='index'),
    path('natural_forest/', forest, name='natural_forest')
]
