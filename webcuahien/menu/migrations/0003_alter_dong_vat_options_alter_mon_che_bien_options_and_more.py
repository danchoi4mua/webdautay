# Generated by Django 5.1 on 2024-09-04 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_animal_dong_vat_rename_dish_mon_che_bien_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dong_vat',
            options={'verbose_name': '2. Dong Vat'},
        ),
        migrations.AlterModelOptions(
            name='mon_che_bien',
            options={'verbose_name': '3. Mon Che Bien'},
        ),
        migrations.AlterModelOptions(
            name='nhom_dong_vat',
            options={'verbose_name': '1. Nhom Dong Vat'},
        ),
    ]
