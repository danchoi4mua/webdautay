# Generated by Django 5.1 on 2024-09-04 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_dong_vat_options_alter_mon_che_bien_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mon_che_bien',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]
