from django.conf import settings

def font_processor(request):
    # Đặt font mặc định hoặc tính toán font dựa trên yêu cầu
    lang_code = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'en')
    if lang_code == 'jp':
        font_family = 'Protest Strike,sans-serif'
    elif lang_code == 'kr':
        font_family = 'Montserrat,sans-serif'
        color = "#c33130"
    elif lang_code == 'en':
        font_family = 'Montserrat,sans-serif'
        color = "#c33130"
    elif lang_code == 'cn':
        font_family = 'Montserrat,sans-serif'
        color = "#FFFFFF"    
    elif lang_code == 'vn':
        font_family = 'Montserrat,sans-serif'
        color = "#c33130"
    elif lang_code == 'th':
        font_family = 'Montserrat,sans-serif'
        color = "#c33130"
    else:
        font_family = 'Arial, sans-serif'
        color = "#c33130"

    return {'font_family': font_family,"color":color }