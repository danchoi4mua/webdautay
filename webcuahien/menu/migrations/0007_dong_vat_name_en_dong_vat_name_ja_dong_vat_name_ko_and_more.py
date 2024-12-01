# Generated by Django 5.1 on 2024-11-25 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_dong_vat_is_visible_dong_vat_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dong_vat',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dong_vat',
            name='name_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dong_vat',
            name='name_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dong_vat',
            name='name_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dong_vat',
            name='name_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='dong_vat',
            name='name_zh_hans',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='description_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='description_ko',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='description_th',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='description_vi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='description_zh_hans',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='name_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='name_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='name_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='name_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='mon_che_bien',
            name='name_zh_hans',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nhom_dong_vat',
            name='name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nhom_dong_vat',
            name='name_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nhom_dong_vat',
            name='name_ko',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nhom_dong_vat',
            name='name_th',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nhom_dong_vat',
            name='name_vi',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='nhom_dong_vat',
            name='name_zh_hans',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
