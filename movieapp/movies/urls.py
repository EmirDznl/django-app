from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name= "home"),
    path("movies", views.movies, name= "movies"),
    path("movies/<int:id>", views.details, name="details"),
]