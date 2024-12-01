from django.shortcuts import render


# Create your views here.
def vechungtoi(request):
    # lang_code = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'default_language_code')
    return render(request,"templates_vechungtoi/templates_vechungtoi.html")


