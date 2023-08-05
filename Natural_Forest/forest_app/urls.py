from django.urls import path

from forest_app.views import forest


urlpatterns = [
    path('natural_forest/', forest, name='forest')
]
