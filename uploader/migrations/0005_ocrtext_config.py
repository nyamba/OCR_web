# Generated by Django 2.1.7 on 2019-06-14 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_ocrtext_execution_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocrtext',
            name='config',
            field=models.TextField(default='', verbose_name='OCR config'),
        ),
    ]