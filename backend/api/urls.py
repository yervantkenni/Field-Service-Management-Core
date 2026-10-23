from django.urls import path

from api import views

urlpatterns = [
    path("", views.root, name="root"),
    path("health", views.health, name="health"),
]
