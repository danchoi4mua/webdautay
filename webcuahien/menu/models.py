from django.db import models

class Nhom_Dong_vat(models.Model):
    name = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)
    def __str__(self):
        # Trả về tên của loại động vật
        return self.name


class Dong_vat(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Nhom_Dong_vat, on_delete=models.CASCADE, related_name='animals')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_visible = models.BooleanField(default=True)  
    def __str__(self):
        # Trả về tên của động vật
        return self.name


class Mon_Che_Bien(models.Model):
    name = models.CharField(max_length=100)
    animal = models.ForeignKey(Dong_vat, on_delete=models.CASCADE, related_name='dishes')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    def __str__(self):
        # Trả về tên của món ăn
        return self.name

