# Generated by Django 2.2 on 2019-06-17 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elderhouse', '0002_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='created_at',
            field=models.DateTimeField(default='created at'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='updated_at',
            field=models.DateTimeField(default='updated at'),
        ),
    ]
