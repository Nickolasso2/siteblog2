from django.urls import path
from .views import *

urlpatterns = [
    path('', show_journey, name = 'menu'),
]