from unicodedata import name
from django.urls import URLPattern, path 
from . import views
import datetime

urlpatterns = [
    path("hello/", views.file2),
    path("welcomepage/", views.file4),
    path("helloworld/", views.file5),
    path("mybirthday/", views.date),
    path("greet/", views.greet),
    path("foli/", views.list, name="foodlist"),
    path("forms/", views.form, name="forms1"),
]