from django.db import models

# Create your models here.
class Tuyen_Dung(models.Model):
    cong_viec_can_tuyen = models.CharField(max_length=100)
    mo_ta_cong_viec =models.TextField()
    yeu_cau_cong_viec =models.TextField()
    quyen_loi = models.TextField()
    def __str__(self):
        # Trả về tên của món ăn
        return self.cong_viec_can_tuyen