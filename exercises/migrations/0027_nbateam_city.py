# Generated by Django 2.2.1 on 2020-03-24 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0026_remove_nbateam_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='nbateam',
            name='city',
            field=models.CharField(default='las vegas', max_length=255),
            preserve_default=False,
        ),
    ]