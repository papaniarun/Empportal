# Generated by Django 3.0.2 on 2020-01-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200113_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='dob',
            field=models.CharField(max_length=255),
        ),
    ]
