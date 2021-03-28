from django.urls import path
from test_site_1 import views

urlpatterns = [
    path("test/", views.test),
]