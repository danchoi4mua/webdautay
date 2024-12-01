from django.shortcuts import render
from django.utils.translation import gettext ,activate
from django.http import JsonResponse
from django.conf import settings

# Create your views here.
def trangchu(request):
    # lang_code = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'default_language_code')
    return render(request,"templates_trangchu/templates_trangchu.html")



# def custom_404_view(request, exception=None):
#     return render(request, '404.html', status=404)

# def custom_500_view(request):
#     return render(request, '500.html', status=500)

# def custom_403_view(request, exception=None):
#     return render(request, '403.html', status=403)

# def custom_400_view(request, exception=None):
#     return render(request, '400.html', status=400)



# def set_language_ajax(request):
#     lang_code = request.GET.get('lang_code')
#     if lang_code:
#         activate(lang_code)
#         response = JsonResponse({'status': 'success'})
#         response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
#         return response
#     return JsonResponse({'status': 'error'}, status=400)