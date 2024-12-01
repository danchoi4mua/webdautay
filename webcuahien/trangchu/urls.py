from django.urls import path

from . import views

urlpatterns = [
    path("", views.trangchu, name="trangchu"),

]
#    path('set_language_ajax/', views.set_language_ajax, name='set_language_ajax'),
