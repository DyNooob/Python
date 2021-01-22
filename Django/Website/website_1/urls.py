from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('talk/', talk, name="talk"),
    path('talk_up/', talk_up, name='search')
]
