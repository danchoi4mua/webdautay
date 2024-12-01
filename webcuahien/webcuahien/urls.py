"""
URL configuration for webcuahien project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns


# handler404 = views.custom_404_view
# handler500 = views.custom_500_view
# handler403 = views.custom_403_view
# handler400 = views.custom_400_view

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('menu/', include("menu.urls"), name='menu'),
    path('tuyendung/', include("reservation.urls"), name='tuyendung'),
    path('vechungtoi/', include("vechungtoi.urls"), name='vechungtoi'),
    path('', include("trangchu.urls"), name='trangchu'),
    path('rosetta/', include('rosetta.urls'), name='rosetta'),  # Thêm dòng này
    path('i18n/', include('django.conf.urls.i18n'), name='i18n'),  # Thêm dòng này
]
