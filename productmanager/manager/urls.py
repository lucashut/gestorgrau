from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("inspector/", views.inspector, name="inspector"),
    path("search/", views.search, name="search")
]