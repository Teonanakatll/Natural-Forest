from django.urls import path

from fairy_forest_app.views import fairy_forest

urlpatterns = [
    path('fairy_forest/', fairy_forest, name='fairy_forest')
]