# Generated by Django 3.0.2 on 2020-01-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200113_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]