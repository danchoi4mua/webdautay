from django.urls import path

from . import views

urlpatterns = [
    path("", views.tuyedung, name="tuyendung"),
    path('<int:pk>',views.congviec, name="congviec"),

]