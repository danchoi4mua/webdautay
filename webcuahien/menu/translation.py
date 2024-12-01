from modeltranslation.translator import register, TranslationOptions
from .models import Nhom_Dong_vat , Dong_vat , Mon_Che_Bien



@register(Nhom_Dong_vat)
class Nhom_Dong_vatTranslationOptions(TranslationOptions):
    fields = ('name',)  # Các trường cần dịch
    
@register(Dong_vat)
class Dong_vatTranslationOptions(TranslationOptions):
    fields = ('name',)  # Các trường cần dịch
    
@register(Mon_Che_Bien)
class Mon_Che_BienTranslationOptions(TranslationOptions):
    fields = ('name','description')  # Các trường cần dịch