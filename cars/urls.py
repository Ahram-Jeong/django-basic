from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    # html의 name 값과 path의 name 값이 연결
    path("list/", views.list, name = "list"),
    path("add/", views.add, name = "add"),
    path("delete/", views.delete, name = "delete"),
]