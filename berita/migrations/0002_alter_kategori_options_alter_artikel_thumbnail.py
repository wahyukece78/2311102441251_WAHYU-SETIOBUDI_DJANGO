# Generated by Django 5.1.7 on 2025-03-14 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('berita', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategori',
            options={'verbose_name_plural': '1. Kategori'},
        ),
        migrations.AlterField(
            model_name='artikel',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='artikel'),
        ),
    ]
