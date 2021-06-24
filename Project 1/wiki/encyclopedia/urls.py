from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.page, name="page"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("upload", views.upload, name="upload"),
    path("existingpage", views.existing, name="existingpage"),
    path("wiki/edit/<str:name>", views.edit, name="edit"),
    path("random", views.random, name="random"),
]
