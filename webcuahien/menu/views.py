from django.shortcuts import render
from django.utils.translation import gettext ,activate
from .models import Nhom_Dong_vat, Dong_vat, Mon_Che_Bien





def menu_view(request):
    groups = Nhom_Dong_vat.objects.filter(is_visible=True).prefetch_related('animals__dishes')
    return render(request, 'templates_menu/templates_menu.html',{'groups': groups})



