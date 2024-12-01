from django.urls import path

from . import views

urlpatterns = [
    path("", views.vechungtoi, name="vechungtoi"),
]