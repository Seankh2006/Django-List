
from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.file1),
    path("<str:name>", views.file3),
]